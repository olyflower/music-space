from django.contrib.auth import get_user_model
from django.db import models

from core.models import BaseModel


class Track(BaseModel):
    title = models.CharField(max_length=200)
    length = models.IntegerField(null=True, blank=True)
    artist = models.CharField(max_length=200, blank=True)
    create_date = models.DateField(null=True, blank=True)
    track_file = models.FileField(upload_to="tracks/", blank=True)
    album = models.ForeignKey(to="music.Album", related_name="tracks", on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)


class Playlist(BaseModel):
    playlist_title = models.CharField(max_length=200)
    track = models.ManyToManyField(to="music.Track", related_name="playlists")
    user = models.ForeignKey(to=get_user_model(), on_delete=models.CASCADE)


class Album(BaseModel):
    album_title = models.CharField(max_length=200)
    text = models.CharField(max_length=150)
    genre = models.ForeignKey(to="music.Genre", null=True, related_name="genres", on_delete=models.CASCADE)
    image = models.ImageField(default="default.png", upload_to="media/covers")


class Genre(BaseModel):
    genre_title = models.CharField(max_length=200)
    description = models.TextField(max_length=1200, blank=True)
