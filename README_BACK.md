# BACKEND
영화추천 프로그램을 만들기로 하여서, 
아래와 같은 기능을 팀원과 함께 논의하여 구현 하였습니다.

1. 커뮤니티 기능 (게시글 생성, 삭제, 수정 / 댓글 생성, 삭제, 수정)
2. 영화추천 기능
3. 영화 리스트 화면, 영화 클릭 시 상세 정보와 한줄감상평(생성, 삭제, 수정)
4. 로그인, 로그아웃, 회원가입 -> dj_rest_auth, dj_rest_auth_registration 사용

<hr>

## 1. ERD 
### movies/models.py
* movie, movie에 달릴 comment의 관계 1:N 
* user와 comment의 관계 1:N 
* genre와 movie는 ManytoMany로 설정 -> 데이터를 보면 영화 하나당 다양한 장르를 가지고 있음, 장르 또한 여러가지 영화와 관계가 있으므로 ManytoMany로 하였음.

### articles/models.py
* user와 article의 관계 1:N
* article과 comment의 관계 1:N
* commnet와 user의 관계 1:N



<hr>


## 2. tmdb에서 데이터 요청
* 모델을 작성한 후 field에 맞게 영화정보를 요청하여 json 파일로 저장, loaddata를 이용하여 DB에 영화정보를 저장하였음.
* tmdb는 아래의 api로 요청을 보내면 인기순으로 20개씩 영화 데이터를 응답한다.
```pytohn
<https://api.themoviedb.org/3/movie/popular?
api_key=><<api_key>>&language=<<language>>&page=<<page>>
```
* for문을 이용하여 위의 api로 10번의 요청을 보내서 데이터를 저장하였다. 
* 데이터를 보기 편하게 하기위해 indent="\t" 옵션을 설정하였다. 
### 문제 1. 
* 데이터를 불러오는 도중 비어있는 정보들이 있는 것을 발견하였다.
* genres가 비어있는 경우에 영화추천 기능에 문제를 일으킬 수 있어, 필터링을 하였다.
### 문제 2. 
* loaddata를 이용해 서버에 저장하려고 하니 아래의 에러가 발생하였다.
```
django.core.serializers.base.DeserializationError: Problem installing fixture...
```
* 원인 : django에 맞는 JSON형식을 맞추지 않아서 생긴 오류
* 해결 : 아래의 형식을 맞추어 다시 저장하였음.

```
[
	{
		'model' : 'movies.movie',
		'pk' :  movie['id'],
		'fields' : {
        	"....." : "......etc..."
        }
    }
]
```

```python
import json
import requests

def get_genre_data():
    genre_data = []
    API_KEY = ''
    API_URL = f'https://api.themoviedb.org/3/genre/movie/list?api_key={API_KEY}&language=ko'
    API_RESPONSE = requests.get(API_URL).json().get('genres')
    
    for genre in API_RESPONSE:
        fields = {
            'genre' : genre['name']    
        }
        data = {
            'model' : 'movies.genre',
            'pk' : genre['id'],
            'fields' : fields 
        }

        genre_data.append(data)
    with open('genre_data.json', 'w', encoding='utf-8') as w:
        json.dump(genre_data, w, indent="", ensure_ascii=False)
    
def get_movie_data():
    movie_data = []

    API_KEY = ''
    index = 1
    for i in range(1, 10):
        API_URL = f'https://api.themoviedb.org/3/movie/popular?api_key={API_KEY}&language=ko&page={i}'
        API_RESPONSE = requests.get(API_URL).json().get('results')
        
        for movie in API_RESPONSE:
            if movie.get('genres', ''):
                fields = {
                    'title' : movie['title'],
                    'poster_url' : movie['poster_path'],
                    'overview' : movie['overview'],
                    'vote_avg' : movie['vote_average'],
                    'release_date' : movie['release_date'],
                    'genres' : movie['genre_ids'],
                }
                data = {
                    'model' : 'movies.movie',
                    'pk' :  movie['id'],
                    'fields' : fields
                }
                movie_data.append(data)
    with open('movie_data.json', 'w', encoding='utf-8') as w : 
        json.dump(movie_data, w, indent="", ensure_ascii=False)

get_movie_data()
get_genre_data()
```

## 3. serializers.py 작성

* django에 있는 모델 인스턴스를 REST API 에서 사용하는 JSON 형태로 변환하기 위해 작성하였다.
* CommentSerializer 안에 UserSerializer를 작성하면(nested objects), User 정보를 같이 응답해준다.
* serializer 모델에 대입하는 인자는 하나의 객체 인스턴스여야 한다. 따라서 queryset이나 객체 리스트를 넣으면 에러가 발생한다.
-> 이때, 쿼리 셋이나 객체로 생성된 리스트를 허용하는 인자가 many=True 
```python
# nested objects 예제. 
# 응답 [{"id":1,"content":"test_movie_comment","score":4.5,"user":{"id":1,"username":"kayden"}}]

class CommentSerializer(serializers.ModelSerializer):

    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('id', 'username')

    user = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'content', 'score', 'user',)
        read_only_fields = ('movie_comments',)
```

## 4. views.py 작성 (영화추천 기능 구현)
* 정보 조회, 상세정보 조회, 댓글 생성, 삭제, 수정 기능은 거의 비슷하므로 코드는 올리지 않겠습니다.
### 영화 추천 알고리즘을 구현하였습니다.
* 사용자가 좋아요를 한 영화 정보를 기반으로, 그 영화의 장르를 가져와서 같은 장르의 영화를 추천하는 알고리즘입니다
* serializer를 새로 작성하여 하려했으나 'str object has no "__meta"' error가 발생했고, 어디가 문제인지 찾질 못해
기존의 정보에서 뽑아서 작성하였습니다.
```python
movies/views.py->reco_movie

@api_view(['GET'])
def reco_movie(request):
    is_userlike = False 
    genre_name = '' 
    if request.user.like_movies.all(): # 좋아요 한 영화가 있을 경우.
        is_userlike = True
        gnr_cnt = dict()
        like_movies = request.user.like_movies.all()
        for i in like_movies:
            m_pk = i.id # 좋아요를 한 영화의 pk를 찾고 Movie의 인스턴스에서 해당 pk와 일치하는 영화를 가져옴
            movie = Movie.objects.get(pk=m_pk) # movie라는 변수에 할당하였음.
            genres = movie.genres.all() # 특정 movie의 장르를 genres에 할당
            for genre in genres: # for문을 통해 
                gnr_cnt[genre.pk] = gnr_cnt.get(genre.pk, 0) + 1 # 어떤 장르를 가장 좋아하는지 선택한 장르에 대한 누적합을 통해 구한다.
        fav_gnr = sorted(gnr_cnt.items(), key=lambda x:x[1], reverse=True)[0][0]  # 정렬, 가장 많은 장르의 pk를 fav_gnr에 할당
        # RESPONSE -> {12: 2, 14: 2, 28: 2, 878: 1, 10770: 1, 35: 1}

        # 장르 이름 구하기
        # 장르 이름을 구해서 이런 장르는 어떠세요라는 문구를 출력할때 쓰기 위해 장르의 이름을 구하는 코드
        genres = list(Genre.objects.all())
        for genre in genres:
            if fav_gnr == genre.id:
                genre_name = genre.genre

        # fav_gnr에 해당하는 영화 목록을 movies에 할당        
        movies = list(Movie.objects.filter(genres=fav_gnr).all())
    else: # 좋아요 한 영화가 없을 경우.
        # 평점이 8점 이상인 영화 목록을 movies에 할당 __gte를 사용하여 평점 8점 이상인 것을 뽑아옴.
        
        movies = list(Movie.objects.filter(vote_avg__gte=8).all())
    
    # Response 될 데이터 
    movie = choice(movies) # 랜덤으로 하나를 pick
    
    serializer = MovieSerializer(movie)
    context = {
        'is_userlike' : is_userlike,
        'genre_name' : genre_name,
        'user' : request.user.username,
        'movie' : serializer.data,
    }
    return Response(context)

```

