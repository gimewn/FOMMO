import router from '@/router'
import axios from 'axios'
import drf from '@/api/drf'

export default {
  state: {
    movies:[],
    movie:{},
    reco_movie:{}
  },
  getters: {
    movies: state => state.movies,
    movie: state => state.movie,
    reco_movie: state => state.reco_movie
  },
  mutations: {
    SET_MOVIES: (state, movies) => state.movies = movies,
    SET_MOVIE: (state, movie) => state.movie = movie,
    SET_MOVIE_COMMENTS:(state, comments) => (state.movie.movie_comments = comments),
    SET_RECO_MOVIE:(state, movie) => state.reco_movie = movie
  },
  actions: {
    fetchMovies({commit, getters}){
      axios({
        url: drf.movies.movies(),
        method:'get',
        headers:getters.authHeader
      })
        .then(res => commit('SET_MOVIES', res.data))
        .catch(err => console.error(err.response))
    },
    fetchMovie({commit, getters}, moviePk){
      axios({
        url:drf.movies.movie(moviePk),
        method:'get',
        headers: getters.authHeader
      })
        .then(res => {
          console.log(res.data)
          commit('SET_MOVIE', res.data)
        })
        .catch(err => {
          if (err.response.status == 404){
            router.push({name:'NotFound404'})
          }
        })
    },
    createMovieComment({commit, getters}, {moviePk, datas}){
      axios({
        url:drf.movies.createMovieComment(moviePk),
        method:'post',
        data:datas,
        headers:getters.authHeader
      })
        .then(res => commit('SET_MOVIE_COMMENTS', res.data))
        .catch(err => console.error(err.response))
    },
    editMovieComment({commit, getters}, {moviePk, commentPk, content, score}){
      axios({
        url:drf.movies.editMovieComment(moviePk, commentPk),
        method:'put',
        data:{content, score},
        headers:getters.authHeader
      })
        .then(res => commit('SET_MOVIE_COMMENTS', res.data))
        .catch(err => console.error(err.response))
    },
    deleteMovieComment({commit, getters}, {moviePk, commentPk}){
      axios({
        url:drf.movies.deleteMovieComment(moviePk, commentPk),
        method:'delete',
        data:{},
        headers:getters.authHeader
      })
        .then(res => commit('SET_MOVIE_COMMENTS', res.data))
        .catch(err => console.error(err.response))
    },
    fetchRecoMovie({commit, getters}){
      axios({
        url:drf.movies.recoMovie(),
        method:'get',
        headers:getters.authHeader
      })
        .then(res => {
          commit('SET_RECO_MOVIE', res.data)
        })
    }
  },
  modules: {
  }
}
