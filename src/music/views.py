from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DeleteView, DetailView, ListView

from music.models import FavoriteTrack, Genre, Playlist, Track
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


class PlaylistDetailView(LoginRequiredMixin, DetailView):
    login_url = "core:login"
    redirect_field_name = "index"
    template_name = "music/playlist_detail.html"
    model = Playlist


class GetFavoriteTrackView(LoginRequiredMixin, ListView):
    login_url = "core:login"
    redirect_field_name = "index"
    template_name = "music/favourite_tracks.html"
    model = FavoriteTrack


class AddToFavoritesView(View):
    def post(self, request, pk):
        track = Track.objects.get(pk=pk)
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


def tracks(request, count):
    generate_tracks.delay(count)
    return HttpResponse("Task started")


def test(request):
    test_task.delay()
    return HttpResponse("Task started")
