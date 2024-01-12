from django.urls import path
from . import views

urlpatterns = [
    # first arg - url endpoint
    # second arg - view to render
    # third arg - names the route
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('cats/', views.cats_index, name='index'),
]