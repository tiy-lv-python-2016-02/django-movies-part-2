from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import Avg


class Movie(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=100, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def rating_count(self):
        return self.rating_set.count()

    @property
    def average_rating(self):
        rating = self.rating_set.aggregate(avg=Avg('rating_value'))
        return rating['avg']

    @property
    def all_ratings(self):
        # all users that rated this film
        return self.rating_set.all()


    def __str__(self):
        return self.title


class Rater(models.Model):

    # Switch to options
    gender = models.CharField(max_length=1, null=True)
    age = models.IntegerField(null=True, validators=[MinValueValidator(1),
                                                     MaxValueValidator(150)]
                              )
    occupation = models.CharField(max_length=50, null=True)
    zip_code = models.CharField(max_length=9, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def all_ratings(self):
        return self.rating_set.all()

    def __str__(self):
        return str(self.id)


class Rating(models.Model):
    movie = models.ForeignKey(Movie)
    rater = models.ForeignKey(Rater)
    created_at = models.DateTimeField(auto_now_add=True)

    rating_value = models.FloatField(help_text="Enter a rating (1-10)",
                                     validators=[MinValueValidator(1),
                                                 MaxValueValidator(10)])

























