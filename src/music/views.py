from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.views.generic import ListView

from music.models import Track


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
