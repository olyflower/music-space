from django.urls import include, path
from rest_framework import routers

from api.views import (AlbumViewSet, ArtistViewSet, CustomerViewSet,
                       GenreViewSet, PlaylistCreateView, PlaylistListView,
                       PlaylistRetrieveDeleteView, PlaylistUpdateView,
                       TrackCreateView, TrackDeleteView, TrackListView,
                       TrackRetrieveView, TrackUpdateView)

app_name = "api"
router = routers.DefaultRouter()
router.register("customers", CustomerViewSet)
router.register("genres", GenreViewSet)
router.register("artists", ArtistViewSet)
router.register("albums", AlbumViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("music/track/", TrackListView.as_view(), name="track_list"),
    path("music/track/<int:pk>/", TrackRetrieveView.as_view(), name="track_retrieve"),
    path("music/track/<int:pk>/update/", TrackUpdateView.as_view(), name="track_update"),
    path("music/track/<int:pk>/delete/", TrackDeleteView.as_view(), name="track_delete"),
    path("music/track/create/", TrackCreateView.as_view(), name="track_create"),
    path("music/playlist/", PlaylistListView.as_view(), name="playlist_list"),
    path("music/playlist/<int:pk>/", PlaylistRetrieveDeleteView.as_view(), name="playlist_retrieve_delete"),
    path("music/playlist/<int:pk>/update/", PlaylistUpdateView.as_view(), name="playlist_update"),
    path("music/playlist/create/", PlaylistCreateView.as_view(), name="playlist_create"),
]
