from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
import os


def index(request):
    return JsonResponse({"key": os.environ["AUTH_TOKEN"]})
