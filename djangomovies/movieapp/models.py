from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import Avg


class Rater(models.Model):
    """
    settings for Rater model
    """
    MALE = 'M'
    FEMALE = 'F'

    genders = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    )
    gender = models.CharField(max_length=6, choices=genders, null=True,
                              blank=True)
    age = models.CharField(max_length=3)
    occupation = models.CharField(max_length=150)
    zip_code = models.CharField(max_length=5)

    def __str__(self):
        return str(self.id)


class Movie(models.Model):
    """
    settings for the movie model
    """
    title = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    genre = models.CharField(max_length=200, blank=True)
    rater = models.ForeignKey(Rater, blank=True, null=True)

    def __str__(self):
        return self.title

    def avg_rating(self):
        """
        returns average rating of the movies rating set
        """
        rating = self.rating_set.aggregate(avg=Avg('rating'))
        return rating['avg']


class Rating(models.Model):
    """
    settings for the rating model
    """
    rating = models.FloatField(
        validators=[MinValueValidator(0.1), MaxValueValidator(10.0)])
    movie = models.ForeignKey(Movie)
    rater = models.ForeignKey(Rater, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

