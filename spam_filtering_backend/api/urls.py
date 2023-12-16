"""Endpoints for the API app"""
from django.urls import path

from . import views

urlpatterns = [
    path("auth", views.authenticate, name="authenticate"),
    path("classify", views.classify, name="classify"),
]
