from django.urls import path
from . import views

urlpatterns = [
    # first arg - url endpoint
    # second arg - view to render
    # third arg - names the route
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('cats/', views.cats_index, name='index'),
    
    # route for the detail page of our cats
    # we need an id, as well as a way to refer to the id
    path('cats/<int:cat_id>', views.cats_detail, name='detail'),
    path('cats/create', views.CatCreate.as_view(),  name='cats_create'),
    path('cats/<int:pk>/update', views.CatUpdate.as_view(), name='cats_update'),
    path('cats/<int:pk>/delete', views.CatDelete.as_view(), name='cats_delete'),
]