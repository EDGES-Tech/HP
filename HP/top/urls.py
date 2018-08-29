from django.urls import include, path
from . import views


app_name = 'top'
urlpatterns = [
    path('top', views.top,name='top')
]