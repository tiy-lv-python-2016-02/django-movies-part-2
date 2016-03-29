from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from moviesite.models import Movie, Rater


def list_movies(request):
    """
    Since database queries can't be sorted on a property I did that sorting
    here. There is probably a better way to do this.
    :return: A sorted list of the 20 highest rated movies.
    """
    all_movies = Movie.objects.all()
    movies = sorted(all_movies,
                    key=lambda x: x.average_rating,
                    reverse=True)[:20]
    return render(request, "moviesite/movie_list.html", {"movies": movies})


def movie_detail(request, id):
    movie = get_object_or_404(Movie, pk=id)
    time_run = timezone.now()

    return render(request, "moviesite/movie_detail.html", {"movie": movie,
                  "time_run": time_run})


def rater_detail(request, id):
    rater = get_object_or_404(Rater, pk=id)
    rater_ratings = rater.all_ratings
    time_run = timezone.now()

    return render(request, "moviesite/rater_detail.html",
                  {"rater": rater,
                   "rater_ratings": rater_ratings,
                   "time_run": time_run})
