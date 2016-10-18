from django.conf.urls import url, include

from accounts import views
from django.contrib.auth.views import login, logout

urlpatterns = [
    url(r'^login/', login, {'template_name': 'login.html'}),
    url(r'^reg/', views.registration),
]