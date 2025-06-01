
from django.contrib import admin
from django.urls import path , include
from . import views

urlpatterns = [
    path('list/', views.movie_list, name='movie_list'),
    path('list/<int:pk>/', views.movie_detail, name='movie_detail'),
    path('', include('imdb_api.urls')),
]
