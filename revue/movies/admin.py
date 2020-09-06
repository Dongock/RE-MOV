from django.contrib import admin
from .models import Movie, Genre

class GenreAdmin(admin.ModelAdmin):
    list_display=['kname']
admin.site.register(Genre, GenreAdmin)

class MovieAdmin(admin.ModelAdmin):
    list_display=['ktitle', 'release_date']
admin.site.register(Movie, MovieAdmin)