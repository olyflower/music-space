import random

from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from faker import Faker

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

    def get_absolute_url(self):
        return reverse("music:track_detail", kwargs={"pk": self.pk})

    def __str__(self):
        return f"{self.title} ({self.pk})"

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)

    @classmethod
    def generate_instances(cls, count):
        faker = Faker()
        for _ in range(count):
            cls.objects.create(
                title=faker.sentence(),
                length=random.randint(50, 500),
                create_date=faker.date(),
                artist=random.choice(Artist.objects.all()),
                album=random.choice(Album.objects.all()),
            )


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

    @classmethod
    def generate_instances(cls, count):
        faker = Faker()
        for _ in range(count):
            cls.objects.create(title=faker.sentence(), genre=random.choice(Genre.objects.all()))


class Artist(BaseModel):
    name = models.CharField(max_length=200)
    biography = models.TextField(default="biography", null=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

    @classmethod
    def generate_instances(cls, count):
        faker = Faker()
        for _ in range(count):
            cls.objects.create(
                name=faker.name(),
            )


class Genre(BaseModel):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=1200, blank=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("music:genre_detail", kwargs={"pk": self.pk})
