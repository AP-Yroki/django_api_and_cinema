from rest_framework import serializers
from .models import Director, Films, Poster, Genre

class FilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Films
        fields = "__all__"

class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = "__all__"

class PosterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poster
        fields = "__all__"

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"