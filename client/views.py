from django.shortcuts import render, render_to_response
from django.http import Http404, HttpResponse
from django.template.loader import get_template
from django.template import Context

from django.contrib import auth
from django import forms


class AuthForm(forms.Form):
    login = forms.CharField(widget=forms.EmailInput)
    password = forms.CharField(widget=forms.PasswordInput)

def main_page(request):

    # Redirect to login page
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/client/login/')

    t = get_template('client_main.html')
    html = t.render(Context())
    return HttpResponse(html)

