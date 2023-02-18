from django.core.exceptions import ValidationError
from django.test import TestCase

from core.utils.samples import sample_track


class TestMusicModel(TestCase):
    def setUp(self):
        self.test_track = sample_track(title="test_track")

    def tearDown(self):
        self.test_track.delete()

    def test_title_limit(self):
        with self.assertRaises(ValidationError):
            sample_track(title="A" * 7000)
