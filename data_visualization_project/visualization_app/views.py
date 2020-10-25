from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('hello')

def interactive_plot(request):
    return HttpResponse('here is the interactive plot page')

def static_plot(request):
    return HttpResponse('here is the static plot page')