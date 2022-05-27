from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

from movies.models import Movie


class User(AbstractUser):
    like_movies= models.ManyToManyField(Movie, blank=True, related_name='user')
