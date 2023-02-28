from music.models import Album, Artist, Track


def sample_track(title, **params):
    default = {"artist": Artist.objects.create(), "album": Album.objects.create()}
    default.update(params)
    return Track.objects.create(title=title, **default)
