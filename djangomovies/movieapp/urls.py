from django.conf.urls import url
from movieapp.views import top_20, movie_detail, rater_detail

urlpatterns = [
    url(r'^movie_detail/(?P<id>)\d+/$', movie_detail, name="movie_detail"),
    url(r'^rater_detail/(?P<id>)\d+/$', rater_detail, name="rater_detail"),
    url(r'^top_20/$', top_20, name="top_20")
]