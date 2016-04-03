from django.contrib import admin
from movieapp.models import Movie, Rating, Rater


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'genre', 'date_added', 'avg_rating')


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('id', 'movie', 'rating', 'rater', 'date_added')


@admin.register(Rater)
class RaterAdmin(admin.ModelAdmin):
    list_display = ('id', 'gender', 'age', 'occupation', 'zip_code')