from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from music.forms import PlaylistForm
from music.models import Album, Artist, FavoriteTrack, Genre, Playlist, Track
from music.tasks import (generate_albums, generate_artists, generate_genres,
                         generate_tracks, test_task)


class GetTracksView(LoginRequiredMixin, ListView):
    login_url = "core:login"
    redirect_field_name = "index"
    template_name = "music/tracks_list.html"
    model = Track

    def get_queryset(self):
        search = self.request.GET.get("search_text")
        search_fields = ["title", "artist__name", "album__title"]
        if search:
            or_filter = Q()
            for field in search_fields:
                or_filter |= Q(**({f"{field}__icontains": search}))
            return Track.objects.filter(or_filter)

        return Track.objects.all()


class TrackDetailView(LoginRequiredMixin, DetailView):
    login_url = "core:login"
    redirect_field_name = "index"
    template_name = "music/track_detail.html"
    model = Track


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


class GetPlaylistView(LoginRequiredMixin, ListView):
    login_url = "core:login"
    redirect_field_name = "index"
    template_name = "music/playlist_list.html"
    model = Playlist


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


class ArtistDetailView(LoginRequiredMixin, DetailView):
    login_url = "core:login"
    redirect_field_name = "index"
    template_name = "music/artist_detail.html"
    model = Artist


class AlbumDetailView(LoginRequiredMixin, DetailView):
    login_url = "core:login"
    redirect_field_name = "index"
    template_name = "music/album_detail.html"
    model = Album


class AddToFavoritesView(View):
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


def track_count(request):
    tracks = Track.objects.order_by("-play_count")
    return render(request, "music/top_tracks.html", {"tracks": tracks})


def genres(request):
    generate_genres.delay()
    return HttpResponse("Task started")


def artists(request, count):
    generate_artists.delay(count)
    return HttpResponse("Task started")


def albums(request, count):
    generate_albums.delay(count)
    return HttpResponse("Task started")


def tracks(request, count):
    generate_tracks.delay(count)
    return HttpResponse("Task started")


def test(request):
    test_task.delay()
    return HttpResponse("Task started")
