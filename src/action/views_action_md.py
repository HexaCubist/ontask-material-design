# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function

import pytz
from django.db import IntegrityError
from django.utils.html import format_html

from action.views_out import session_dictionary_name
from logs.models import Log
from visualizations.plotly import PlotlyHandler

try:
    import urlparse
    from urllib import urlencode
except:  # For Python 3
    import urllib.parse as urlparse
    from urllib.parse import urlencode

import django_tables2 as tables
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test, login_required
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from django.http import Http404, JsonResponse
from django.shortcuts import redirect, reverse, render
from django.template.loader import render_to_string
from django.views import generic
from django.views.decorators.clickjacking import xframe_options_exempt
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

from action.evaluate import render_template
from dataops import ops, pandas_db
from ontask.permissions import UserIsInstructor, is_instructor
from ontask.tables import OperationsColumn
from workflow.ops import get_workflow
from .forms import (
    ActionUpdateForm,
    ActionForm,
    EditActionOutForm,
    EnableURLForm,
    ActionDescriptionForm, ActionImportForm
)
from action.ops import (
    serve_action_in,
    serve_action_out,
    clone_action,
    do_export_action,
    do_import_action,
    get_workflow_action)
from .models import Action, Condition

from .views_action import *
from dataops.formula_evaluation import evaluate_node_sql, get_variables
from logs.models import Log
from ontask.permissions import is_instructor, UserIsInstructor
from workflow.ops import get_workflow
from .forms import ConditionForm, FilterForm

@user_passes_test(is_instructor)
def action_index(request, wid=None):
    """
    Render the list of actions attached to a workflow.
    :param request: Request object
    :return: HTTP response with the table.
    """

    # Get the appropriate workflow object
    workflow = get_workflow(request, wid=wid)
    if not workflow:
        return redirect('workflow:index')

    # Reset object to carry action info throughout dialogs
    request.session[session_dictionary_name] = {}
    request.session.save()

    # Get the actions
    actions = Action.objects.filter(workflow__id=workflow.id).order_by('-modified')

    # Context to render the template
    context = {'has_table': ops.workflow_has_table(workflow), 'workflow': workflow}

    # Build the table only if there is anything to show (prevent empty table)
    qset = []
    for action in actions:
        qset.append({'id': action.id,
                     'name': action.name,
                     'description_text': action.description_text,
                     'action_type': action.get_action_type_display(),
                     'action_tval': action.action_type,
                     'is_out': action.is_out,
                     'is_executable': action.is_executable,
                     'last_executed_log': action.last_executed_log,
                     'serve_enabled': action.serve_enabled,
                     'modified': action.modified})

    context['table'] = \
        ActionTable(qset, orderable=False)
    context['no_actions'] = len(qset) == 0
    context['qset'] = qset

    return render(request, 'action/md_index.html', context)


@user_passes_test(is_instructor)
def edit_action(request, pk):
    """
    View to select the right action edit procedure
    :param request: Request object
    :param pk: Action PK
    :return: HTML response
    """

    # Try to get the workflow first
    workflow = get_workflow(request)
    if not workflow:
        return redirect('workflow:index')

    if workflow.nrows == 0:
        messages.error(
            request,
            _('Workflow has no data. Go to "Manage table data" to upload data.')
        )
        return redirect(reverse('action:index'))

    # Get the action and the columns
    try:
        action = Action.objects.filter(
            Q(workflow__user=request.user) |
            Q(workflow__shared=request.user)
        ).distinct().prefetch_related('columns').get(pk=pk)
    except ObjectDoesNotExist:
        return redirect('action:index')

    if action.action_type == Action.PERSONALIZED_TEXT:
        return edit_action_out(request, workflow, action)

    if action.action_type == Action.PERSONALIZED_JSON:
        return edit_action_out(request, workflow, action)

    if action.action_type == Action.SURVEY:
        return edit_action_in(request, workflow, action)

    if action.action_type == Action.TODO_LIST:
        return redirect(reverse('under_construction'), {})
        # return edit_action_in(request, workflow, action)


def edit_action_out(request, workflow, action):
    """
    View to handle the form to edit an action OUT (editor, conditions,
    filters, etc).
    :param request: Request object
    :param action: Action
    :return: HTML response
    """

    # Create the form
    form = EditActionOutForm(request.POST or None, instance=action)

    # Get the filter or None
    filter_condition = action.get_filter()

    # Conditions to show in the page.
    conditions = Condition.objects.filter(
        action=action, is_filter=False
    ).order_by('created')

    # Context to render the form
    context = {'filter_condition': filter_condition,
               'action': action,
               'conditions': conditions,
               'query_builder_ops': workflow.get_query_builder_ops_as_str(),
               'attribute_names': [x for x in workflow.attributes.keys()],
               'column_names': workflow.get_column_names(),
               'selected_rows':
                   filter_condition.n_rows_selected if filter_condition else -1,
               'has_data': ops.workflow_has_table(action.workflow),
               'total_rows': workflow.nrows,
               'form': form,
               'vis_scripts': PlotlyHandler.get_engine_scripts(),
               'workflow': workflow
               }

    # Template to use
    template = 'action/md_edit_personalized_text.html'
    if action.action_type == Action.PERSONALIZED_JSON:
        template = 'action/edit_personalized_json.html'

    # Processing the request after receiving the text from the editor
    if request.method == 'GET' or not form.is_valid():
        # Return the same form in the same page
        return render(request, template, context=context)

    # Get content
    content = form.cleaned_data.get('content', None)

    # Render the content as a template and catch potential problems.
    # This seems to be only possible if dealing directly with Jinja2
    # instead of Django.
    try:
        render_template(content, {}, action)
    except Exception as e:
        # Pass the django exception to the form (fingers crossed)
        form.add_error(None, e.message)
        return render(request, template, context)

    # Log the event
    Log.objects.register(request.user,
                         Log.ACTION_UPDATE,
                         action.workflow,
                         {'id': action.id,
                          'name': action.name,
                          'workflow_id': workflow.id,
                          'workflow_name': workflow.name,
                          'content': content})

    # Text is good. Update the content of the action
    action.set_content(content)

    # Update additional fields
    if action.action_type == Action.PERSONALIZED_JSON:
        action.target_url = form.cleaned_data['target_url']

    action.save()

    return redirect('action:index')

class ActionCreateView(UserIsInstructor, generic.TemplateView):
    """
    CBV to handle the create action form (very simple)
    """
    form_class = ActionForm
    template_name = 'action/includes/md_partial_action_create.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return save_action_form(request,
                                form,
                                self.template_name)

    def post(self, request):
        form = self.form_class(request.POST)
        return save_action_form(request,
                                form,
                                self.template_name)
