from django.shortcuts import render
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib import auth
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.shortcuts import render_to_response

class AuthForm(forms.Form):
    username = forms.EmailField(widget=forms.EmailInput)
    password = forms.CharField(widget=forms.PasswordInput)

def registration(request):
    if request.method == 'POST':
        form = AuthForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.create_user(username=data['username'], password=data['password'])
            user.save()

#            user = auth.authenticate(username=data['username'], password=data['password'])
            if user is not None and user.is_active:
                return HttpResponseRedirect('/client/')
            else:
                return render_to_response('login.html', {'error': form.errors})
        else:
            return render_to_response('login.html', {'error': form.errors})
    else:
        return render_to_response('login.html', {'error': form.errors})