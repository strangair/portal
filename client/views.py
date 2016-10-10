from django.shortcuts import render
from django.http import Http404, HttpResponse
from django.template.loader import get_template
from django.template import Context

def main_page(request):
    t = get_template('client_main.html')
    html = t.render(Context())
    return HttpResponse(html)
