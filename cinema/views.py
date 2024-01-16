from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, \
    CreateAPIView

from .models import Films, Director, Genre, Poster
from .serializers import (FilmSerializer, DirectorSerializer, GenreSerializer,
                          PosterSerializer)


class FilmAPIView(ListAPIView, CreateAPIView):
    queryset = Films.objects.all()
    serializer_class = FilmSerializer


class FilmAPIDetal(RetrieveUpdateDestroyAPIView):
    queryset = Films.objects.all()
    serializer_class = FilmSerializer


class DirectorAPIView(ListAPIView, CreateAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer


class DirectorAPIDetal(RetrieveUpdateDestroyAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer


class GenreAPIView(ListAPIView, CreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class GenreAPIDetal(RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class PosterAPIView(ListAPIView, CreateAPIView):
    queryset = Poster.objects.all()
    serializer_class = PosterSerializer


class PosterAPIDetal(RetrieveUpdateDestroyAPIView):
    queryset = Poster.objects.all()
    serializer_class = PosterSerializer
