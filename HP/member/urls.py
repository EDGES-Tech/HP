# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

app_name = 'member'
urlpatterns = [
    url('index', views.member, name='member'),
]