"""Endpoints for the Storage app"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r"mails", views.MailViewSet, basename="mails")

urlpatterns = [path("", include(router.urls))]
