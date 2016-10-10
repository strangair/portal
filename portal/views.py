# coding: utf-8

from django.http import Http404, HttpResponse
from django.template.loader import get_template
from django.template import Context

def main_page(request):
    t = get_template('main.html')
    html = t.render(Context())
    return HttpResponse(html)

