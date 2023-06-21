from django.urls import path
from . import views

urlpatterns = [
    # This first path tells me that it's looking in views.py for a class that's named Home at localhost:8000/
    path('', views.Home.as_view(), name='home'),
    path('about/', views.About.as_view(), name='about'),
    path('artists/', views.ArtistList.as_view(), name="artist_list"),
    path('songs/', views.SongList.as_view(), name="song_list"),
    # This is telling me if I hit the URL artists/new, I should see a class named ArtistCreate in the views
    path('artists/new/', views.ArtistCreate.as_view(), name="artist_create")
]