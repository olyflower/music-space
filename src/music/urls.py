from django.urls import path

from music.views import (GenreDetailView, GetGenresView, GetPlaylistView,
                         GetTracksView, PlaylistDetailView, TrackDetailView,
                         albums, artists, genres, tracks)

app_name = "music"

urlpatterns = [
    path("track_list/", GetTracksView.as_view(), name="get_tracks"),
    path("genre_list/", GetGenresView.as_view(), name="get_genres"),
    path("playlist_list/", GetPlaylistView.as_view(), name="get_playlist"),
    path("genre/<int:pk>/", GenreDetailView.as_view(), name="genre_detail"),
    path("track/<int:pk>/", TrackDetailView.as_view(), name="track_detail"),
    path("playlist/<int:pk>/", PlaylistDetailView.as_view(), name="playlist_detail"),
    path("generate-artists/<int:count>/", artists, name="generate_artists"),
    path("generate-genres", genres, name="generate_genres"),
    path("generate-albums/<int:count>/", albums, name="generate_albums"),
    path("generate-tracks/<int:count>/", tracks, name="generate_tracks"),
]
