from django.urls import path

from music.views import (GenreDetailView, GetGenresView, GetTracksView,
                         TrackDetailView)

app_name = "music"

urlpatterns = [
    path("track_list/", GetTracksView.as_view(), name="get_tracks"),
    path("genre_list/", GetGenresView.as_view(), name="get_genres"),
    path("genre/<int:pk>/", GenreDetailView.as_view(), name="genre_detail"),
    path("track/<int:pk>/", TrackDetailView.as_view(), name="track_detail"),
]
