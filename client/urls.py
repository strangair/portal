from django.conf.urls import url, include

from client import views

urlpatterns = [
    url(r'^client/', views.main_page, name='main'),
]