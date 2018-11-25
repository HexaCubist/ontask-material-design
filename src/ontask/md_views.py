# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import generic
from django.views.decorators.clickjacking import xframe_options_exempt
from django.views.decorators.csrf import csrf_exempt

from action import settings
from django_auth_lti.decorators import lti_role_required
from ontask.permissions import UserIsInstructor
from ontask.tasks import increase_track_count
from ontask.permissions import is_instructor, is_admin
from workflow.md_views import workflow_index

def home(request):
    if not request.user.is_authenticated:
        # Unauthenticated request, go to login
        return redirect(reverse('accounts:login'))

    if is_instructor(request.user) or is_admin(request.user):
        # Authenticated request, go to the workflow index
        return workflow_index(request)

    # Authenticated request from learner, show profile
    return redirect(reverse('profiles:show_self'))
