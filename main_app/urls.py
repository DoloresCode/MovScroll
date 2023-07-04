from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"), 
    path('about/', views.About.as_view(), name='about'),
    path('actors/', views.ActorList.as_view(), name='actor_list'), 
    path('movies/', views.MovieList.as_view(), name="movie_list"),
    path('actor/new/', views.ActorCreate.as_view(), name="actor_create"),
    path('actor/<int:pk>/', views.ActorDetail.as_view(), name="actor_detail"),
    path('actors/<int:pk>/update', views.ActorUpdate.as_view(), name="actor_update"),
    path('actors/<int:pk>/delete', views.ActorDelete.as_view(), name="actor_delete"),
    path('actors/<int:pk>/movies/new/', views.MovieCreate.as_view(), name="movie_create"),
    path('watchlists/<int:pk>/movies/<int:movie_pk>/', views.WatchlistMovieAssoc.as_view(), name="watchlist_movie_assoc"),
    path('watchlists/', views.WatchlistList.as_view(), name="watchlist_list"),
    path('watchlist/<int:pk>/', views.WatchlistDetail.as_view(), name='watchlist_detail'),
    path('movie/new/', views.MovieCreateGeneral.as_view(), name="movie_create_general"),
    path('movies/<int:pk>/update', views.MovieUpdate.as_view(), name="movie_update"),
    path('movies/<int:pk>/delete', views.MovieDelete.as_view(), name="movie_delete"),
    path('watchlists/new/', views.WatchlistCreate.as_view(), name="watchlist_create"),
    path('watchlists/<int:pk>/delete', views.WatchlistDelete.as_view(), name='watchlist_delete'),
    path('watchlists/<int:pk>/update', views.WatchlistUpdate.as_view(), name="watchlist_update"),
]