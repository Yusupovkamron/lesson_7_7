from django.contrib.admin import action
from django.db.transaction import atomic
from rest_framework.decorators import action
from rest_framework.pagination import LimitOffsetPagination
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Artist, Albom, Songs, Country
from .serializers import ArtistSerializer, SongsSerializer, AlbomSerializer, CountrySerializer
import json
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import TokenAuthentication


class LandingPageAPIView(APIView):
    def get(self, request):
        return Response(data={"message": "Hi laze developers"})

    def post(self, request):
        return Response(data={"post api": "this is post api"})


class ArtistApiView(APIView):
    def get(self, request):
        artists = Artist.objects.all()
        serialisers = ArtistSerializer(artists, many=True)
        return Response(data=serialisers.data)


class AlbomAPIViewSet(ModelViewSet):
    queryset = Albom.objects.all()
    serializer_class = AlbomSerializer

    @action(detail=True, methods=["GET"])
    def albom(self, request, *args, **kwargs):
        song = self.get_object()
        albom = song.albom
        serializer = AlbomSerializer(albom)
        return Response(data=serializer.data)




class SongSetAPIView(ModelViewSet):
    queryset = Songs.objects.all()
    serializer_class = SongsSerializer
    authentication_classes = (TokenAuthentication,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ['^title']
    pagination_class = LimitOffsetPagination

    @action(detail=True, methods=["GET"])
    def listen(self, request, *args, **kwargs):
        song = self.get_object()
        with atomic():
            song.listened += 1
            song.save()
            return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=False, methods=["GET"])
    def top(self, request, *args, **kwargs):
        songs = self.get_queryset()
        songs = songs.order_by('-listened')[:2]
        serializer = SongsSerializer(songs, many=True)
        return Response(data=serializer.data)

class CountrySetApiView(ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    authentication_classes = (TokenAuthentication,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ['^title']
    pagination_class = LimitOffsetPagination
