from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"), 
    path('about/', views.About.as_view(), name='about'),
    path('actors/', views.ActorList.as_view(), name='actor_list'), 
    path('movies/', views.MovieList.as_view(), name="movie_list"),
    path('actor/new/', views.ActorCreate.as_view(), name="actor_create")
]