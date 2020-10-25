from django.urls import include, path
from visualization_app import views

urlpatterns = [
    path('', views.index),
    path('interactive', views.interactive_plot),
    path('static', views.static_plot)

]