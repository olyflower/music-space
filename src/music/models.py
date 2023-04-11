import random

from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from faker import Faker

from core.models import BaseModel


class Track(BaseModel):
    title = models.CharField(max_length=200, blank=False)
    length = models.PositiveIntegerField(null=True, blank=True)
    artist = models.ForeignKey(to="music.Artist", related_name="artist", on_delete=models.CASCADE)
    create_date = models.DateField(null=True, blank=True)
    track_file = models.FileField(upload_to="tracks/", blank=False, null=False)
    album = models.ForeignKey(to="music.Album", related_name="tracks", on_delete=models.CASCADE)
    play_count = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["title"]

    def get_absolute_url(self):
        return reverse("music:track_detail", kwargs={"pk": self.pk})

    def __str__(self):
        return f"{self.title} ({self.pk})"

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)


class Playlist(BaseModel):
    title = models.CharField(max_length=200, default="Playlist")
    tracks = models.ManyToManyField(to="music.Track", related_name="playlist_tracks")
    user = models.ForeignKey(to=get_user_model(), on_delete=models.CASCADE)

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("music:playlist_detail", kwargs={"pk": self.pk})


class Album(BaseModel):
    title = models.CharField(max_length=200, blank=False, null=False)
    description = models.TextField(default="description", null=True)
    genre = models.ForeignKey(to="music.Genre", null=True, related_name="genres", on_delete=models.CASCADE)
    image = models.ImageField(default="default.png", upload_to="covers/")

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("music:album_detail", kwargs={"pk": self.pk})

    @classmethod
    def generate_instances(cls, count):
        faker = Faker()
        for _ in range(count):
            cls.objects.create(title=faker.sentence(), genre=random.choice(Genre.objects.all()))


class Artist(BaseModel):
    name = models.CharField(max_length=200, blank=False, null=False)
    biography = models.TextField(default="biography", null=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("music:artist_detail", kwargs={"pk": self.pk})

    @classmethod
    def generate_instances(cls, count):
        faker = Faker()
        for _ in range(count):
            cls.objects.create(
                name=faker.name(),
            )


class Genre(BaseModel):
    name = models.CharField(max_length=200, blank=False)
    description = models.TextField(max_length=1200, blank=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("music:genre_detail", kwargs={"pk": self.pk})

    @classmethod
    def generate_genres(cls):
        genres_data = [
            {
                "name": "Rock",
                "description": "Rock music is a broad genre of popular music that originated "
                "as Rock and Roll in the United States in the late 1940s and early 1950s, "
                "developing into a range of different styles in the mid-1960s and later, "
                "particularly in the United States and the United Kingdom.",
            },
            {
                "name": "Pop",
                "description": "Pop is a genre of popular music that originated in its modern form "
                "during the mid-1950s in the United States and the United Kingdom. "
                "The terms popular music and pop music are often used interchangeably, "
                "although the former describes all music that is popular and includes "
                "many disparate styles.",
            },
            {
                "name": "Hip Hop",
                "description": "Hip-hop and Rap music are mainly described as stylized rhythmic "
                "music with the fast rhyming singing style called rap. The two genres "
                "are closely related and originated from the Afro-American and "
                "Latin-American ghettos in the U.S.A. in the mid-’70s. "
                "The music has its own culture with breakdance, MCing, DJing, "
                "and graffiti. ",
            },
            {
                "name": "Jazz",
                "description": "Jazz is a music genre that originated in the African-American communities "
                "of New Orleans, Louisiana, United States, in the late 19th and "
                "early 20th centuries, with its roots in blues and ragtime.",
            },
            {
                "name": "Blues",
                "description": "A genre and musical form developed by African Americans in the "
                "United States around the end of the 19th century from African-American "
                "work songs and European-American folk music. The blues form, "
                "ubiquitous in jazz and rock and roll, is characterized by the "
                "call-and-response pattern, the blues scale and specific chord progressions, "
                "of which the twelve-bar blues is the most common. Blues shuffles or "
                "walking bass reinforce the trance-like rhythm and form a repetitive "
                "groove effect.",
            },
            {
                "name": "Country",
                "description": "Also known as country and western, country music has its roots in "
                "the south of the USA. Having evolved from a combination of different "
                "fold styles. Combining the influence of working-class immigrants it "
                "takes its cues from Irish and Celtic folk, traditional English ballads "
                "and cowboy songs. In the modern era, there are numerous sub-genres "
                "like country pop, country rock and neo-country.",
            },
            {
                "name": "Folk",
                "description": "A genre that evolved from traditional music during the 20th century folk "
                "revival. One meaning often given is that of old songs with no known "
                "composers; another is music that has been transmitted and evolved by a "
                "process of oral transmission or performed by custom over a long period "
                "of time.",
            },
            {
                "name": "Reggae",
                "description": "Reggae music originated from Jamaica during the late 1960s. "
                "Reggae is characterized by its distinctive vocals and lyrics, "
                "which talk about the Jamaican people’s lifestyles, struggles, "
                "and social aspects. The songs are generally activist songs "
                "trying to raise awareness on world peace, anti-racism, anti-capitalism, "
                "anti-colonialism as well as the Rastafari movement.",
            },
            {
                "name": "R&B",
                "description": "A genre of popular African-American music that originated in the 1940s as "
                "urbane, rocking, jazz based music with a heavy, insistent beat. "
                "Lyrics focus heavily on the themes of triumphs and failures in terms "
                "of relationships, freedom, economics, aspirations, and sex.",
            },
            {
                "name": "Soul",
                "description": "A popular music genre that combines elements of African-American gospel "
                "music, rhythm and blues and jazz.",
            },
            {
                "name": "Funk",
                "description": "Funk is a music genre that originated in African American communities "
                "in the mid-1960s when musicians created a rhythmic, danceable new form "
                "of music through a mixture of soul, jazz, and rhythm and blues (R&B).",
            },
        ]

        for data in genres_data:
            cls.objects.create(name=data["name"], description=data["description"])


class FavoriteTrack(BaseModel):
    user = models.ForeignKey(to=get_user_model(), on_delete=models.CASCADE)
    track = models.ForeignKey(to="music.Track", on_delete=models.CASCADE)
