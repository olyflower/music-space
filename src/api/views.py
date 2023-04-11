from django.contrib.auth import get_user_model
from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, RetrieveAPIView,
                                     RetrieveDestroyAPIView, UpdateAPIView)
from rest_framework.viewsets import ModelViewSet

from api.serializers import (AlbumSerializer, ArtistSerializer,
                             CustomerSerializer, GenreSerializer,
                             PlaylistSerializer, TrackSerializer)
from music.models import Album, Artist, Genre, Playlist, Track


class CustomerViewSet(ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = CustomerSerializer


class TrackListView(ListAPIView):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer


class TrackRetrieveView(RetrieveAPIView):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer


class TrackCreateView(CreateAPIView):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer


class TrackDeleteView(DestroyAPIView):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer


class TrackUpdateView(UpdateAPIView):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer


class GenreViewSet(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class ArtistViewSet(ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


class AlbumViewSet(ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class PlaylistListView(ListAPIView):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer


class PlaylistRetrieveDeleteView(RetrieveDestroyAPIView):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer


class PlaylistCreateView(CreateAPIView):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer


class PlaylistUpdateView(UpdateAPIView):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer
