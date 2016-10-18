from django.shortcuts import render

class AuthForm(forms.Form):
    login = forms.CharField(widget=forms.EmailInput)
    password = forms.CharField(widget=forms.PasswordInput)

def login(request):
    t = get_template('client_main.html')
    html = t.render(Context())
    return HttpResponse(html)