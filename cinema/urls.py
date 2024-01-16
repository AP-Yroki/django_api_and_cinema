from django.urls import path

# from .views import ProductGet
from .views import (FilmAPIView, FilmAPIDetal, GenreAPIView, GenreAPIDetal,
                    PosterAPIView, DirectorAPIDetal, PosterAPIDetal,
                    DirectorAPIView)

urlpatterns = [
    path('films/',FilmAPIView.as_view()),
    path('film/<int:pk>', FilmAPIDetal.as_view()),
    path('genres/',GenreAPIView.as_view()),
    path('genre/<int:pk>', GenreAPIDetal.as_view()),
    path('posters/', PosterAPIView.as_view()),
    path('poster/<int:pk>', PosterAPIDetal.as_view()),
    path('directors/', DirectorAPIView.as_view()),
    path('director/<int:pk>', DirectorAPIDetal.as_view()),
]