from django.contrib import admin

from .models import Films, Poster, Director, Genre


admin.site.register(Films)
admin.site.register(Poster)
admin.site.register(Director)
admin.site.register(Genre)