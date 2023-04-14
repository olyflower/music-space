from django.urls import path

from music.views import (AddToFavoritesView, AlbumAddView, AlbumDetailView,
                         ArtistAddView, ArtistDetailView, CreatePlaylistView,
                         DeleteFavoriteTrackView, DeletePlaylistView,
                         GenreDetailView, GetAlbumsView, GetArtistsView,
                         GetFavoriteTrackView, GetGenresView, GetPlaylistView,
                         GetTracksView, PlaylistDetailView, TrackDetailView,
                         TrackUploadView, UpdatePlaylistView, UploadView,
                         albums, artists, genres)

app_name = "music"

urlpatterns = [
    path("track_list/", GetTracksView.as_view(), name="get_tracks"),
    path("track_upload/", TrackUploadView.as_view(), name="track_upload"),
    path("add_album/", AlbumAddView.as_view(), name="add_album"),
    path("add_artist/", ArtistAddView.as_view(), name="add_artist"),
    path("upload/", UploadView.as_view(), name="upload"),
    path("genre_list/", GetGenresView.as_view(), name="get_genres"),
    path("playlist_list/", GetPlaylistView.as_view(), name="get_playlist"),
    path("genre/<int:pk>/", GenreDetailView.as_view(), name="genre_detail"),
    path("track/<int:pk>/", TrackDetailView.as_view(), name="track_detail"),
    path("artist_list/", GetArtistsView.as_view(), name="get_artists"),
    path("artist/<int:pk>/", ArtistDetailView.as_view(), name="artist_detail"),
    path("album_list/", GetAlbumsView.as_view(), name="get_albums"),
    path("album/<int:pk>/", AlbumDetailView.as_view(), name="album_detail"),
    path("playlist/<int:pk>/", PlaylistDetailView.as_view(), name="playlist_detail"),
    path("favorite-tracks/", GetFavoriteTrackView.as_view(), name="favourite_tracks"),
    path("add-to-favorite/<int:pk>/", AddToFavoritesView.as_view(), name="add_to_favorite"),
    path("favorite-tracks/<int:pk>/delete/", DeleteFavoriteTrackView.as_view(), name="delete_favourite_track"),
    path("generate-artists/<int:count>/", artists, name="generate_artists"),
    path("generate-genres", genres, name="generate_genres"),
    path("generate-albums/<int:count>/", albums, name="generate_albums"),
    path("playlist/create/", CreatePlaylistView.as_view(), name="playlist_create"),
    path("playlist/<int:pk>/edit/", UpdatePlaylistView.as_view(), name="playlist_edit"),
    path("playlist/<int:pk>/delete/", DeletePlaylistView.as_view(), name="playlist_delete"),
]
