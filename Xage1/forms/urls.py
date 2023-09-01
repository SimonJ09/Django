from django.contrib import admin
from django.urls import path
from django.urls import path, include
from . import views

urlpatterns = [
    path("forms/", views.forms_view, name='forms'),
]
