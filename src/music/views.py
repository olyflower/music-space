from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  TemplateView, UpdateView)

from music.forms import (AlbumAddForm, ArtistAddForm, PlaylistForm,
                         TrackUploadForm)
from music.models import Album, Artist, FavoriteTrack, Genre, Playlist, Track
from music.tasks import generate_albums, generate_artists, generate_genres


class GetTracksView(LoginRequiredMixin, ListView):
    login_url = "core:login"
    redirect_field_name = "index"
    template_name = "music/tracks_list.html"
    model = Track

    def get_queryset(self):
        sort_by = self.request.GET.get("sort")
        if sort_by == "artist":
            return Track.objects.order_by("artist__name")
        else:
            search = self.request.GET.get("search_text")
            search_fields = ["title", "artist__name", "album__title", "album__genre__name", "length", "create_date"]
            if search:
                or_filter = Q()
                for field in search_fields:
                    or_filter |= Q(**({f"{field}__istartswith": search}))
                return Track.objects.filter(or_filter)

            return Track.objects.all()


class TrackDetailView(LoginRequiredMixin, DetailView):
    login_url = "core:login"
    redirect_field_name = "index"
    template_name = "music/track_detail.html"
    model = Track


class TrackUploadView(LoginRequiredMixin, CreateView):
    model = Track
    form_class = TrackUploadForm
    template_name = "music/track_upload.html"
    success_url = reverse_lazy("music:get_tracks")

    def form_valid(self, form):
        form.instance.user = self.request.user
        title = form.cleaned_data["title"]
        artist = form.cleaned_data["artist"]
        album = form.cleaned_data["album"]
        if Track.objects.filter(title=title, artist=artist, album=album).exists():
            form.add_error(None, "Track already exists!")
            return self.form_invalid(form)
        else:
            return super().form_valid(form)


class AlbumAddView(LoginRequiredMixin, CreateView):
    model = Album
    template_name = "music/add_album.html"
    success_url = reverse_lazy("music:upload")
    form_class = AlbumAddForm

    def form_valid(self, form):
        if Album.objects.filter(title=form.cleaned_data["title"]).exists():
            form.add_error(None, "This album has already been added!")
            return self.form_invalid(form)
        else:
            return super().form_valid(form)


class ArtistAddView(LoginRequiredMixin, CreateView):
    model = Artist
    template_name = "music/add_artist.html"
    success_url = reverse_lazy("music:upload")
    form_class = ArtistAddForm

    def form_valid(self, form):
        if Artist.objects.filter(name=form.cleaned_data["name"]).exists():
            form.add_error(None, "This artist already exists!")
            return self.form_invalid(form)
        else:
            return super().form_valid(form)


class UploadView(LoginRequiredMixin, TemplateView):
    login_url = "core:login"
    template_name = "music/upload.html"


class GetGenresView(LoginRequiredMixin, ListView):
    login_url = "core:login"
    redirect_field_name = "index"
    template_name = "music/genre_list.html"
    model = Genre


class GenreDetailView(LoginRequiredMixin, DetailView):
    login_url = "core:login"
    redirect_field_name = "index"
    template_name = "music/genre_detail.html"
    model = Genre

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["list_tracks"] = Track.objects.filter(album__genre=self.object).order_by("?")[:5]
        return context


class GetPlaylistView(LoginRequiredMixin, ListView):
    login_url = "core:login"
    redirect_field_name = "index"
    template_name = "music/playlist_list.html"
    model = Playlist

    def get_queryset(self):
        return Playlist.objects.filter(user=self.request.user)


class CreatePlaylistView(LoginRequiredMixin, CreateView):
    login_url = "core:login"
    redirect_field_name = "index"
    template_name = "music/playlist_create.html"
    form_class = PlaylistForm
    success_url = reverse_lazy("music:get_playlist")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class UpdatePlaylistView(LoginRequiredMixin, UpdateView):
    template_name = "music/playlist_edit.html"
    form_class = PlaylistForm
    success_url = reverse_lazy("music:get_playlist")
    queryset = Playlist.objects.all()


class DeletePlaylistView(LoginRequiredMixin, DeleteView):
    success_url = reverse_lazy("music:get_playlist")
    model = Playlist


class PlaylistDetailView(LoginRequiredMixin, DetailView):
    login_url = "core:login"
    redirect_field_name = "index"
    template_name = "music/playlist_detail.html"
    model = Playlist

    def post(self, request, *args, **kwargs):
        playlist = self.get_object()
        if "remove_track" in request.POST:
            track_id = int(request.POST["remove_track"])
            track = get_object_or_404(Track, pk=track_id)
            playlist.tracks.remove(track)

        return self.get(request, *args, **kwargs)


class GetFavoriteTrackView(LoginRequiredMixin, ListView):
    login_url = "core:login"
    redirect_field_name = "index"
    template_name = "music/favourite_tracks.html"
    model = FavoriteTrack

    def get_queryset(self):
        queryset = super().get_queryset().filter(user=self.request.user)
        sort = self.request.GET.get("sort")
        if sort == "artist":
            queryset = queryset.order_by("track__artist__name")
        return queryset


class GetArtistsView(LoginRequiredMixin, ListView):
    login_url = "core:login"
    redirect_field_name = "index"
    template_name = "music/artist_list.html"
    model = Artist


class ArtistDetailView(LoginRequiredMixin, DetailView):
    login_url = "core:login"
    redirect_field_name = "index"
    template_name = "music/artist_detail.html"
    model = Artist


class GetAlbumsView(LoginRequiredMixin, ListView):
    login_url = "core:login"
    redirect_field_name = "index"
    template_name = "music/album_list.html"
    model = Album


class AlbumDetailView(LoginRequiredMixin, DetailView):
    login_url = "core:login"
    redirect_field_name = "index"
    template_name = "music/album_detail.html"
    model = Album


class AddToFavoritesView(LoginRequiredMixin, View):
    def post(self, request, pk):
        track = Track.objects.get(pk=pk)
        favorite_track_exists = FavoriteTrack.objects.filter(user=request.user, track=track).exists()
        if not favorite_track_exists:
            favorite_track = FavoriteTrack(user=request.user, track=track)
            favorite_track.save()
        return redirect("music:favourite_tracks")


class DeleteFavoriteTrackView(LoginRequiredMixin, DeleteView):
    template_name = "music/favorite_track_delete.html"
    model = FavoriteTrack
    success_url = reverse_lazy("music:favourite_tracks")

    def get_queryset(self):
        return FavoriteTrack.objects.filter(user=self.request.user)


def genres(request):
    generate_genres.delay()
    return HttpResponse("Task started")


def artists(request, count):
    generate_artists.delay(count)
    return HttpResponse("Task started")


def albums(request, count):
    generate_albums.delay(count)
    return HttpResponse("Task started")
