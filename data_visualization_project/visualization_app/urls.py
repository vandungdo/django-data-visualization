from django.urls import include, path
from visualization_app import views


app_name = 'visualization_app'

urlpatterns = [
    path('interactive', views.interactive_plot, name="interactive"),
    path('static', views.static_plot, name="static")

]