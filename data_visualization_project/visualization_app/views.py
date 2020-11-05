from django.shortcuts import render
from django.http import HttpResponse

from .static import bar_plot

# Create your views here.

def index(request):
    return render(request, 'index.html')

def interactive_plot(request):

    return render(request, 'visualization/interactive.html')

def static_plot(request):
    if request.method == 'POST':
        # print(request.POST['plot-type'])
        bar_plot(request.POST['x-static'],request.POST['y-static'])
    return render(request, 'visualization/static_plot.html')