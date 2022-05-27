from rest_framework import serializers
from ..models import Article
from django.contrib.auth import get_user_model
from .comment import CommentSerializer


User = get_user_model() # 아래의 코드에서 함수가 여러번 실행되므로 빼준 것.

class ArticleSerializer(serializers.ModelSerializer):

    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk', 'username')

    article_comments = CommentSerializer(many=True, read_only = True)
    user = UserSerializer(read_only=True)
    like_users = UserSerializer(read_only=True, many=True)

    class Meta :
        model = Article
        fields = ('pk', 'user', 'title', 'content', 'created_at', 'article_comments','like_users')


class ArticleListSerializer(serializers.ModelSerializer):

    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk','username')

    user = UserSerializer(read_only=True)

    class Meta:
        model = Article
        fields = ( 'pk','user','title',)