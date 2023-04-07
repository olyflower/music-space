import os
import random

from celery import shared_task
from django.conf import settings
from django.core.files import File
from faker import Faker

from music.models import Album, Artist, Genre, Track


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
    filepath = os.path.join(settings.MEDIA_ROOT, "tracks/Imagine-Dragons-Monster.mp3")
    for _ in range(count):
        track = Track.objects.create(
            title=faker.sentence(),
            length=random.randint(100, 600),
            create_date=faker.date(),
            artist=random.choice(Artist.objects.all()),
            album=random.choice(Album.objects.all()),
            play_count=random.randint(1, 100),
        )
        with open(filepath, "rb") as f:
            track.track_file.save("OneRepublic-West-Coast.mp3", File(f))


@shared_task
def generate_genres():
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
        Genre.objects.create(name=data["name"], description=data["description"])
