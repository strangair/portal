from django.shortcuts import render, render_to_response
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.template import Context

from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django import forms


# Redirect to login page /accounts/login/
@login_required
def main_page(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')

    user = auth.authenticate(username=username, password=password)

    if user is not None and user.is_active:
        auth.login(request, user)
        return HttpResponseRedirect('/client/')
    else:
        return HttpResponseRedirect('/accounts/login/')





