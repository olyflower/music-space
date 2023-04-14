from datetime import datetime

from django.core.files.uploadedfile import SimpleUploadedFile

from music.models import Album, Artist, Track


def sample_track(title, track_file=None, **params):
    default = {
        "length": 240,
        "artist": Artist.objects.create(),
        "create_date": datetime.now().date(),
        "album": Album.objects.create(),
        "play_count": 0,
    }
    default.update(params)
    if not track_file:
        track_file = SimpleUploadedFile("test_track.mp3", b"file_content", content_type="audio/mpeg")
    return Track.objects.create(title=title, track_file=track_file, **default)
