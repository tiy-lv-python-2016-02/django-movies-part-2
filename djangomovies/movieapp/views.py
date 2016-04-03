from django.db.models import Avg
from movieapp.models import Movie, Rater
from django.shortcuts import render, get_object_or_404


def movie_detail(request, id):
    """
    gets movie object for movie_detail.html
    404 if none
    """

    movie = get_object_or_404(Movie, pk=id)

    return render(request, "movieapp/movie_detail.html", {"movie": movie})


def rater_detail(request, id):
    """
    gets rater object for rater_detail.html
    404 if none
    """

    rater = get_object_or_404(Rater, pk=id)

    return render(request, "movieapp/rater_detail.html", {"rater": rater})


def top_20(request):
    """
    sorts movies by average rating, displaying first 20
    """
    movies = Movie.objects.annotate(avg_rating=Avg('rating__rating')).order_by(
        "-avg_rating")[:20]

    return render(request, "movieapp/top_20.html", {"movies": movies})
