import json
import requests

def get_genre_data():
    genre_data = []
    API_KEY = 'b5a5f84ebb682062b887779904a32def'
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
        json.dump(genre_data, w, indent="\t", ensure_ascii=False)
    
def get_movie_data():
    movie_data = []

    API_KEY = 'b5a5f84ebb682062b887779904a32def'
    index = 1
    for i in range(1, 10):
        API_URL = f'https://api.themoviedb.org/3/movie/popular?api_key={API_KEY}&language=ko&page={i}'
        API_RESPONSE = requests.get(API_URL).json().get('results')
        
        for movie in API_RESPONSE:
            if movie.get('overview', ''):
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
        json.dump(movie_data, w, indent="\t", ensure_ascii=False)

get_movie_data()
get_genre_data()