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
    return render_to_response('client_main.html')






