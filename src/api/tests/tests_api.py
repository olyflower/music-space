from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework.status import (HTTP_200_OK, HTTP_201_CREATED,
                                   HTTP_401_UNAUTHORIZED,
                                   HTTP_405_METHOD_NOT_ALLOWED)
from rest_framework.test import APIClient

from core.utils.samples import sample_track
from music.models import Album, Artist, Genre


class TestAPI(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.album = Album.objects.create(title="album")
        self.artist = Artist.objects.create(name="Artist")
        self.genre = Genre.objects.create(name="Genre name")
        self.track = sample_track(title="track_title", length=100, artist=self.artist, album=self.album)

        self.user = get_user_model().objects.create(email="test_api@gmail.com")
        self.user.set_password("123456")
        self.user.save()

    def test_track_get_track_detail(self):
        self.client.force_authenticate(user=self.user)
        result = self.client.get(
            reverse(
                "api:track_retrieve",
                kwargs={
                    "pk": self.track.pk,
                },
            )
        )

        self.assertEqual(result.status_code, HTTP_200_OK)
        self.assertEqual(
            result.data,
            {
                "id": self.track.pk,
                "title": "track_title",
                "length": 100,
                "artist": {"id": self.artist.pk, "name": "Artist"},
                "album": {"id": self.album.pk, "title": "album"},
            },
        )

    def test_track_detail_no_access(self):
        result = self.client.get(
            reverse(
                "api:track_retrieve",
                kwargs={
                    "pk": self.track.pk,
                },
            )
        )
        self.assertEqual(result.status_code, HTTP_401_UNAUTHORIZED)

    def test_track_detail_patch_not_allowed(self):
        self.client.force_authenticate(user=self.user)
        result = self.client.patch(
            reverse(
                "api:track_retrieve",
                kwargs={
                    "pk": self.track.pk,
                },
            )
        )
        self.assertEqual(result.status_code, HTTP_405_METHOD_NOT_ALLOWED)

    def test_genre_list_no_access(self):
        result = self.client.get(reverse("api:genre-list"))
        self.assertEqual(result.status_code, HTTP_401_UNAUTHORIZED)

    def test_genre_create(self):
        self.client.force_authenticate(user=self.user)
        result = self.client.post(
            reverse("api:genre-list"),
            {
                "name": self.genre.name,
            },
        )

        self.assertEqual(result.data, {"id": result.data["id"], "name": "Genre name"})
        self.assertEqual(result.status_code, HTTP_201_CREATED)
