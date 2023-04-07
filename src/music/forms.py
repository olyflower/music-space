from django import forms

from .models import Album, Artist, Genre, Playlist, Track


class PlaylistForm(forms.ModelForm):
    class Meta:
        model = Playlist
        fields = ["title", "tracks"]


GENRE_CHOICES = (
    ("Rock", "Rock"),
    ("Pop", "Pop"),
    ("Hip Hop", "Hip Hop"),
    ("Jazz", "Jazz"),
    ("Blues", "Blues"),
    ("Country", "Country"),
    ("Folk", "Folk"),
    ("Reggae", "Reggae"),
    ("R&B", "R&B"),
    ("Soul", "Soul"),
    ("Funk", "Funk"),
)


class TrackUploadForm(forms.ModelForm):
    album_title = forms.CharField(max_length=200)
    artist_name = forms.CharField(max_length=200)
    genre = forms.ChoiceField(choices=GENRE_CHOICES)

    class Meta:
        model = Track
        fields = ["title", "length", "track_file", "genre"]

    def save(self, commit=True):
        track = super().save(commit=False)
        album, created = Album.objects.get_or_create(title=self.cleaned_data["album_title"])
        artist, created = Artist.objects.get_or_create(name=self.cleaned_data["artist_name"])
        album.genre = Genre.objects.get(name=self.cleaned_data["genre"])
        track.album = album
        track.artist = artist
        if commit:
            track.save()
            album.save()
        return track
