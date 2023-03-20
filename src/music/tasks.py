import random

from celery import shared_task
from faker import Faker

from music.models import Artist, Genre, Album, Track


@shared_task
def generate_genres(count):
    genres_lst = [
        "Rock",
        "Pop",
        "Hip Hop",
        "Jazz",
        "Blues",
        "Country",
        "Folk",
        "Reggae",
        "R&B",
        "Soul",
        "Funk"
    ]
    faker = Faker()
    for _ in range(count):
        Genre.objects.create(
            name=random.choice(genres_lst),
            description=faker.sentences(nb=3)
        )


@shared_task
def generate_artists(count):
    faker = Faker()
    for _ in range(count):
        Artist.objects.create(
            name=faker.name(),
        )


@shared_task
def generate_albums(count):
    faker = Faker()
    for _ in range(count):
        Album.objects.create(title=faker.sentence(), genre=random.choice(Genre.objects.all()))


@shared_task
def generate_tracks(count):
    faker = Faker()
    for _ in range(count):
        Track.objects.create(
            title=faker.sentence(),
            length=random.randint(50, 500),
            create_date=faker.date(),
            artist=random.choice(Artist.objects.all()),
            album=random.choice(Album.objects.all())
        )
