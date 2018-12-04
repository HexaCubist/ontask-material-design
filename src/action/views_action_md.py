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
    actions = Action.objects.filter(workflow__id=workflow.id)

    # Context to render the template
    context = {'has_table': ops.workflow_has_table(workflow)}

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
                     'serve_enabled': action.serve_enabled})

    context['table'] = \
        ActionTable(qset, orderable=False)
    context['no_actions'] = len(qset) == 0

    return render(request, 'action/md_index.html', context)

