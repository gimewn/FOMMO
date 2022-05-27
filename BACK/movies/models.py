
from django.db import models
from django.conf import settings
User = settings.AUTH_USER_MODEL

# Create your models here.

class Genre(models.Model):
    genre = models.CharField(max_length=50) 

class Movie(models.Model):
    #fields
    title  = models.CharField(max_length=100) # 영화제목
    poster_url = models.TextField() # 포스터 이미지 
    overview = models.TextField() # 줄거리
    vote_avg = models.FloatField() # 평점
    release_date = models.DateField() # 개봉일
    genres = models.ManyToManyField(Genre, related_name='movies')

class Comment(models.Model):
    #relations
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name = 'movie_comments') # 댓글 달린 영화
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='movie_comments') # 댓글 작성자
    #fields
    content = models.TextField() # 댓글 내용
    score = models.FloatField() # user의 영화 평가 점수 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)