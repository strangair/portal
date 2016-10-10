from django.conf.urls import url, include

from client import views

urlpatterns = [
    url(r'^$', views.main_page, name='Client main'),
]