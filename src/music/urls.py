from django.urls import path

from music.views import (AddToFavoritesView, AlbumDetailView, ArtistDetailView,
                         CreatePlaylistView, DeleteFavoriteTrackView,
                         DeletePlaylistView, GenreDetailView,
                         GetFavoriteTrackView, GetGenresView, GetPlaylistView,
                         GetTracksView, PlaylistDetailView, TrackDetailView,
                         UpdatePlaylistView, albums, artists, genres, test,
                         track_count, tracks)

app_name = "music"

urlpatterns = [
    path("track_list/", GetTracksView.as_view(), name="get_tracks"),
    path("genre_list/", GetGenresView.as_view(), name="get_genres"),
    path("playlist_list/", GetPlaylistView.as_view(), name="get_playlist"),
    path("genre/<int:pk>/", GenreDetailView.as_view(), name="genre_detail"),
    path("track/<int:pk>/", TrackDetailView.as_view(), name="track_detail"),
    path("artist/<int:pk>/", ArtistDetailView.as_view(), name="artist_detail"),
    path("album/<int:pk>/", AlbumDetailView.as_view(), name="album_detail"),
    path("playlist/<int:pk>/", PlaylistDetailView.as_view(), name="playlist_detail"),
    path("favorite-tracks/", GetFavoriteTrackView.as_view(), name="favourite_tracks"),
    path("add-to-favorite/<int:pk>/", AddToFavoritesView.as_view(), name="add_to_favorite"),
    path("favorite-tracks/<int:pk>/delete/", DeleteFavoriteTrackView.as_view(), name="delete_favourite_track"),
    path("tracks/top/", track_count, name="top_tracks"),
    path("generate-artists/<int:count>/", artists, name="generate_artists"),
    path("generate-genres", genres, name="generate_genres"),
    path("generate-albums/<int:count>/", albums, name="generate_albums"),
    path("generate-tracks/<int:count>/", tracks, name="generate_tracks"),
    path("playlist/create/", CreatePlaylistView.as_view(), name="playlist_create"),
    path("playlist/<int:pk>/edit/", UpdatePlaylistView.as_view(), name="playlist_edit"),
    path("playlist/<int:pk>/delete/", DeletePlaylistView.as_view(), name="playlist_delete"),
    path("test-task/", test, name="test_task"),
]
