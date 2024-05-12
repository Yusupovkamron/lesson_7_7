from rest_framework import serializers
from .models import Artist, Albom, Songs, Country


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = "__all__"


class AlbomSerializer(serializers.ModelSerializer):
    artist = ArtistSerializer()

    class Meta:
        model = Albom
        fields = "__all__"


class SongsSerializer(serializers.ModelSerializer):
    albom = AlbomSerializer(read_only=True)

    class Meta:
        model = Songs
        fields = "__all__"


class CountrySerializer(serializers.ModelSerializer):
    country = SongsSerializer(read_only=True)

    class Meta:
        model = Country
        fields = "__all__"