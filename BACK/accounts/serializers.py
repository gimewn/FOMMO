from django.contrib.auth import get_user_model
from rest_framework import serializers

from movies.serializers import MovieSerializer

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    
    like_movies = MovieSerializer(many=True)
    class Meta:
        model = User
        fields = ('id','username','like_movies')


class UserSerializer2(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id','username',)
