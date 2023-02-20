from account.models import Customer
from music.models import Album, Track


def sample_track(title, **params):
    default = {"album": Album.objects.create()}
    default.update(params)
    return Track.objects.create(title=title, **default)


def sample_account(email, password, **params):
    default = {"first_name": "Name", "last_name": "Surname", "password": password}
    default.update(params)
    return Customer.objects.create(email=email, **default)
