from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponse
from django.views.generic import DetailView, ListView

from music.models import Genre, Track
from music.tasks import (generate_albums, generate_artists, generate_genres,
                         generate_tracks)


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


class TrackDetailView(LoginRequiredMixin, DetailView):
    login_url = "core:login"
    redirect_field_name = "index"
    template_name = "music/track_detail.html"
    model = Track


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
