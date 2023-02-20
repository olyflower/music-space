from django.contrib import admin

from music.models import Album, Artist, Genre, Playlist, Track

admin.site.register([Track, Playlist, Album, Artist, Genre])
