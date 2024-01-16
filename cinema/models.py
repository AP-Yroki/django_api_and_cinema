from django.db import models

# Create your models here.

class Director(models.Model):
    full_name = models.CharField(max_length=50)
    birth_year = models.DateField()

    def __str__(self):
        return self.full_name

class Genre(models.Model):
    genre_name = models.CharField(max_length=60)

    def __str__(self):
        return self.genre_name


class Films(models.Model):
    name = models.CharField(max_length=50)
    creation_year = models.DateField()
    country = models.CharField(max_length=60)
    director = models.ForeignKey(Director, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Poster(models.Model):
    date = models.DateField()
    films = models.ForeignKey(Films, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.date)
