from django.contrib.auth import get_user_model
from django.db import models

from core.models import BaseModel


class Track(BaseModel):
    title = models.CharField(max_length=200)
    length = models.IntegerField(null=True, blank=True)
    artist = models.ForeignKey(to="music.Artist", related_name="artist", on_delete=models.CASCADE)
    create_date = models.DateField(null=True, blank=True)
    track_file = models.FileField(upload_to="tracks/", blank=True)
    album = models.ForeignKey(to="music.Album", related_name="tracks", on_delete=models.CASCADE)

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)


class Playlist(BaseModel):
    title = models.CharField(max_length=200)
    tracks = models.ManyToManyField(to="music.Track", related_name="playlist_tracks")
    user = models.ForeignKey(to=get_user_model(), on_delete=models.CASCADE)

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title


class Album(BaseModel):
    title = models.CharField(max_length=200)
    description = models.TextField(default="description", null=True)
    genre = models.ForeignKey(to="music.Genre", null=True, related_name="genres", on_delete=models.CASCADE)
    image = models.ImageField(default="default.png", upload_to="media/covers")

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title


class Artist(BaseModel):
    name = models.CharField(max_length=200)
    biography = models.TextField(default="biography", null=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Genre(BaseModel):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=1200, blank=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name
