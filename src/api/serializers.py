from rest_framework.serializers import ModelSerializer

from account.models import Customer
from music.models import Album, Artist, Genre, Playlist, Track


class CustomerSerializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = ("first_name", "last_name", "email", "password", "is_staff")


class ArtistSerializer(ModelSerializer):
    class Meta:
        model = Artist
        fields = ("id", "name")


class AlbumSerializer(ModelSerializer):
    class Meta:
        model = Album
        fields = ("id", "title")


class TrackSerializer(ModelSerializer):
    artist = ArtistSerializer()
    album = AlbumSerializer()

    class Meta:
        model = Track
        fields = ("id", "title", "length", "artist", "album")

    def create(self, validated_data):
        artist_data = validated_data.pop("artist")
        artist = Artist.objects.create(**artist_data)

        album_data = validated_data.pop("album")
        album = Album.objects.create(**album_data)

        validated_data["artist"] = artist
        validated_data["album"] = album

        track = Track.objects.create(**validated_data)

        return track

    def update(self, instance, validated_data):
        artist_data = validated_data.pop("artist")
        if artist_data:
            artist = instance.artist
            artist.name = artist_data.get("name", artist.name)
            artist.save()

        album_data = validated_data.pop("album")
        if album_data:
            album = instance.album
            album.title = album_data.get("title", album.title)
            album.save()

        return super().update(instance, validated_data)


class GenreSerializer(ModelSerializer):
    class Meta:
        model = Genre
        fields = ("id", "name")


class PlaylistSerializer(ModelSerializer):
    class Meta:
        model = Playlist
        fields = ("id", "title", "tracks", "user")
