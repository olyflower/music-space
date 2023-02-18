from django.contrib import admin

from music.models import Album, Genre, Playlist, Track

admin.site.register([Track, Playlist, Album, Genre])
