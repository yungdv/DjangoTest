from django.urls import path, include
from . import  views

urlpatterns = [
    path('', views.index),
    path('groups', views.groups),
    path('groups/files', views.files),
]