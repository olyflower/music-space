from django import forms

from .models import Album, Artist, Playlist, Track


class PlaylistForm(forms.ModelForm):
    class Meta:
        model = Playlist
        fields = ["title", "tracks"]


class TrackUploadForm(forms.ModelForm):
    class Meta:
        model = Track
        fields = ["title", "track_file", "album", "artist"]


class AlbumAddForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ["title", "description", "genre"]


class ArtistAddForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = ["name", "biography"]
