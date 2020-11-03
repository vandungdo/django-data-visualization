from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'index.html')

def interactive_plot(request):

    return render(request, 'visualization/interactive.html')

def static_plot(request):
    example_dict = {'example':'example variable on django template'}
    return render(request, 'visualization/static.html',context=example_dict)