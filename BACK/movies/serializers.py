from rest_framework import serializers
from .models import Genre, Movie, Comment
from django.contrib.auth import get_user_model

User = get_user_model()

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('genre',)


class CommentSerializer(serializers.ModelSerializer):

    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('id', 'username')

    user = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'content', 'score', 'user', 'movie')
        read_only_fields = ('movie',)


class MovieSerializer(serializers.ModelSerializer):

    movie_comments = CommentSerializer(many=True, read_only=True)
    genres = GenreSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = ('id', 'title','poster_url', 'overview','vote_avg','release_date','genres','movie_comments', 'user')