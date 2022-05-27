from django.shortcuts import render, get_object_or_404
from accounts.serializers import UserSerializer
from movies.serializers import CommentSerializer , MovieSerializer, GenreSerializer
from .models import Genre, Movie, Comment
from accounts.models import User
from random import choice
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.


# 영화 리스트 
@api_view(['GET'])
def get_movies(reqeust):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many = True)
    return Response(serializer.data)


# 영화 상세정보 
@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk = movie_pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)

# 코멘트 목록
@api_view(['GET'])
def get_comment(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    comments = movie.movie_comments.all()
    serializer = CommentSerializer(comments, many=True)
    if not comments:
        return Response()
    return Response(serializer.data)
    

# 코멘트 생성
@api_view(['POST'])
def create_comment(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception = True):
        serializer.save(user=request.user, movie = movie)

        comments = movie.movie_comments.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)





# 코멘트 수정
@api_view(['GET','PUT'])
def edit_comment(request, movie_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    movie = get_object_or_404(Movie, pk=movie_pk)

    if request.user == comment.user:
        serializer = CommentSerializer(instance=comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()

            # 사용자가 댓글을 입력하는 사이에 업데이트된 comment 확인을 위해 -> 최신 코멘트리스트를 반환.
            comments = movie.movie_comments.all()
            serializer = CommentSerializer(comments, many = True)
            return Response(serializer.data)
        else:
            return Response(serializer.data)
    else:
        serializer = CommentSerializer(comment)
        return Response(serializer.data)


# 코멘트 삭제
@api_view(['DELETE'])
def delete_comment(request, movie_pk, comment_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    comment = get_object_or_404(Comment, pk=comment_pk)

    if request.user == comment.user:
        comment.delete()
        # 업데이트된 전체 댓글 목록 반환
        comments = movie.movie_comments.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)


@api_view(["POST"])
def like_movie(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    user = request.user
    isLike = False

    if user.like_movies.filter(pk=movie_pk).exists():
        user.like_movies.remove(movie)
    else:
        user.like_movies.add(movie)
        isLike = True
    context = {
        'isLike': isLike
    }
    return Response(context)

@api_view(["GET"])
def check_like(request, movie_pk):
    user = request.user
    isLike = False
    if user.like_movies.filter(pk=movie_pk).exists():
        isLike = True
    context = {
        'isLike':isLike
    }
    return Response(context)


@api_view(['GET'])
def reco_movie(request):
    is_userlike = False 
    # 장르이름
    genre_name = ''
    if request.user.like_movies.all(): # 좋아요 한 영화가 있을 경우.
        is_userlike = True
        gnr_cnt = dict()
        like_movies = request.user.like_movies.all()
        for i in like_movies:
            m_pk = i.id
            movie = Movie.objects.get(pk=m_pk)
            genres = movie.genres.all()
            for genre in genres:
                gnr_cnt[genre.pk] = gnr_cnt.get(genre.pk, 0) + 1 # 어떤 장르를 가장 좋아하는지 선택한 장르에 대한 누적합을 통해 구한다.
        fav_gnr = sorted(gnr_cnt.items(), key=lambda x:x[1], reverse=True)[0][0] # {12: 2, 14: 2, 28: 2, 878: 1, 10770: 1, 35: 1}

        # 장르 이름 구하기
        genres = list(Genre.objects.all())
        for genre in genres:
            if fav_gnr == genre.id:
                genre_name = genre.genre

        # fav_gnr에 해당하는 영화 목록을 movies에 할당        
        movies = list(Movie.objects.filter(genres=fav_gnr).all())

    else: # 좋아요 한 영화가 없을 경우.
        # 평점이 8점 이상인 영화 목록을 movies에 할당
        movies = list(Movie.objects.filter(vote_avg__gte=8).all())
    
    # Response 될 데이터 
    movie = choice(movies)
    serializer = MovieSerializer(movie)
    context = {
        'is_userlike' : is_userlike,
        'genre_name' : genre_name,
        'user' : request.user.username,
        'movie' : serializer.data,
    }
    return Response(context)


'''
context RESPONSE ->

{
"is_userlike":true,
"genre_name":"모험",
"user":"admin",
"movie":
    {
      "title":"캐리비안의 해적: 세상의 끝에서",
      "poster_url":"/bTotG6tZERQqfKr2TDjwdjW8It4.jpg",
      "overview":"윌 터너와 엘리자베스 스완, 바르보사 선장은 바다괴물 크라켄에 잡아먹힌 잭 스패로우를 구하는 데 도움을 얻기 위해 싱가포르의 해적 사오펭을 찾아간다. 이들은 잭 스패로우가 있어야만 해적연맹의 아홉 영주를 모아 연합함대를 구성할 수 있고, 해적 소탕에 쌍심지를 켠 동인도회사에 맞설 수 있다. 동인도회사의 커틀러 베켓 경은 유령선 플라잉 더치맨과 그 선장 데비 존스를 수하에 거느리게 된 터. 이 힘이 막강해서, 해적 연합함대는 다시 바다의 여신 칼립소에게 도움을 요청하기로 한다.",
      "vote_avg":7.2,
      "release_date":"2007-05-19",
      "genres":[12,14,28]}
    }

'''