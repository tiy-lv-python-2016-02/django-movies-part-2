from django.contrib import admin
from moviesite.models import Movie, Rater, Rating


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ("title", "genre", "average_rating")


@admin.register(Rater)
class RaterAdmin(admin.ModelAdmin):
    list_display = ("id", "gender", "age", "occupation", "zip_code")


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ("rating_value", "movie", "rater", "created_at")
