<template>
  <div class="container">
    <div class="movieContents">
      <div class="contentsPoster">
        <img :src="`https://www.themoviedb.org/t/p/w600_and_h900_bestv2/${movie.poster_url}`" class="detailPoster" alt="">
      </div>
      <div class="contentsElse d-flex flex-column align-items-start">
        <h5 class="movieTitle">{{movie.title}}</h5>
        <p class="moviecategory">{{movieRelease}}</p>
        <p>
          <font-awesome-icon icon="fa-solid fa-star"></font-awesome-icon>
          <span class="moviecategory ms-1">{{movie.vote_avg}}</span>
        </p>
        <p class="moviecategory">이 영화의 장르는?</p>
        <div class="mb-3">
          <span v-for="(g, index) in movie.genres" :key="index" class="mgenre">{{g.genre}}</span>
        </div>
        <span class="moviecategory">줄거리</span>
          <p class="overview detailoverview mt-3" v-if="movie.overview.length">{{movie.overview}}</p>
          <p class="overview detailoverview mt-3" v-if="!movie.overview.length">줄거리가 존재하지 않는 영화입니다.</p>
      </div>
    </div>
    <h4 class="mt-5">{{commentCount}}개의 후기가 있어요!</h4>
    <movie-comment-list :comments="movie.movie_comments"/>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
import MovieCommentList from '../components/MovieCommentList.vue'
import moment from "moment"

export default {
  name:'MovieDetail',
  components:{
    MovieCommentList,
  },
  data(){
    return{
      moviePk: this.$route.params.moviePk,
      movieRelease:null
    }
  },
  computed:{
    ...mapGetters(['movie']),
    commentCount(){
      return this.movie.movie_comments?.length
  },
  },
  methods:{
    ...mapActions(['fetchMovie']),
    formatMovieRelease(){
      moment.locales('ko')
      const ReleaseDate = moment(this.movie.release_date)
      const AfterRelease = ReleaseDate.format("YYYY년 M월 D일")
      this.movieRelease = AfterRelease
    },
  },
  created(){
    this.fetchMovie(this.moviePk)
    this.formatMovieRelease()
  }
}
</script>

<style>
.detailPoster{
  width:100%;
  border-radius: 5px;
  margin-right:20px;
}
.fa-star{
  color:orange;
}

.movieContents{
  display: flex;
  margin: 0 50px;
  justify-content: center;
}
.container{
  justify-content: center;
  align-items: center;
}

@media (max-width:1024px){
  .movieContents{
    flex-direction: column;
  }
  .movieTitle{
    margin-top:20px;
  }
}

@media (min-width:1024px){
  .detailPoster{
    max-width: 25rem;
  }
  .detailoverview {
  max-width:25rem;
}
}
.moviecategory{
  font-weight:600;
}
</style>