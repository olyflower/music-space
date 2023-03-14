from django.contrib import admin

from account.models import UserProfile
from music.models import Album, Artist, Genre, Playlist, Track

admin.site.register([Track, Playlist, Album, Artist, Genre, UserProfile])
