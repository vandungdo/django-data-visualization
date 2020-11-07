from django.shortcuts import render
from django.http import HttpResponse

from .plot import *

# Create your views here.

def index(request):
    delete_file()
    return render(request, 'index.html')

def interactive_plot(request):

    return render(request, 'visualization/interactive.html')

def static_plot(request):
    if request.method == 'POST':
        # print(request.POST['plot-type'])
        if request.POST['plot-type'] == 'Bar Plot':
            static_bar_plot(request.POST['x-static'],request.POST['y-static'])
        elif request.POST['plot-type'] == 'Scatter Plot':
            static_scatter_plot(request.POST['x-static'],request.POST['y-static'])
        elif request.POST['plot-type'] == 'Line Plot':
            static_line_plot(request.POST['x-static'],request.POST['y-static'])
        else:
            static_pie_plot(request.POST['x-static'],request.POST['y-static'])
    return render(request, 'visualization/static_plot.html')