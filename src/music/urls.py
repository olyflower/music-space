from django.urls import path

from music.views import GetTracksView

app_name = "music"

urlpatterns = [
    path("", GetTracksView.as_view(), name="get_tracks"),
]
