from django.core.exceptions import ValidationError
from django.test import TestCase

from core.utils.samples import sample_track
from music.models import Album, Artist


class TestMusicModel(TestCase):
    def setUp(self):
        self.album = Album.objects.create(title="album")
        self.artist = Artist.objects.create(name="Artist")
        self.test_track = sample_track(title="track_title", artist=self.artist)
        self.test_track_1 = sample_track(title="track_title", artist=self.artist, album=self.album)

    def test_track_title_max_length(self):
        with self.assertRaises(ValidationError):
            sample_track(title="A" * 7000)

    def test_create_track_with_params(self):
        self.assertEqual(self.test_track_1.album, self.album)
