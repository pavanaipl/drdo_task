from django.urls import path
from django.conf.urls import url
from .views import *

urlpatterns = [

    url(r'^((?P<pk>\d+)/)*$', UsersDetailsAPI.as_view()),
    url(r'^dashboard/$', dashboard, name='dashboard'),
]