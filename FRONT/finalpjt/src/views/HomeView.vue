<template>
<div>
  <div>
    <carousel v-bind:autoplay="true" v-bind:loop="true" :perPage="1">
      <slide>
        <img class="banner-img" src="@/assets/banner01.png" alt="">
      </slide>
      <slide class="slidetwo">
        <img class="banner-img" src="@/assets/banner02.png" alt="">
        <router-link :to="{name:'recoMovie'}" class="gotoreco">
          <button class="gotorecobtn">지금 바로 알아보기</button>
        </router-link>
      </slide>
    </carousel>
  </div>
  <div class='container overflow-auto'>
    <div class="cards row">
      <div v-for="movie in Movies" :key="movie.id" class="col-6 col-lg-3">
        <b-card
          class="movieCard"
          v-b-modal="'MovieModal'"
          @click="openModal(movie)"
          :img-src="`https://www.themoviedb.org/t/p/w600_and_h900_bestv2/${movie.poster_url}`"
          img-alt="Image"
          img-top
          tag="article"
          border-variant="light"
          bg-image
          hover-zoom>
        </b-card>
      </div>
    </div>
    <b-modal id="MovieModal" v-if="modalData" hide-footer :title="`${modalData.title}`">
      <div class="modal-contents">
        <div>
          <p class="category">{{movieRelease}}</p>
          <p>
            <font-awesome-icon icon="fa-solid fa-star"></font-awesome-icon>
            <span class="ms-1">{{modalData.vote_avg}}</span>
          </p>
          <p class="category">이 영화의 장르는...</p>
          <div class="mb-3">
            <span v-for="(g, index) in modalData.genres" :key="index" class="mgenre">{{g.genre}}</span>
          </div>
          <span class="category">줄거리</span>
          <p class="overview mt-3" v-if="modalData">{{modalData.overview}}</p>
          <p class="overview mt-3" v-if="!modalData">줄거리 정보가 없는 영화입니다.</p>
          <div v-if="modalData.movie_comments.length>0">
            <p>{{modalData.movie_comments.length}}개의 리뷰가 있어요!</p>
            <div class="d-flex justify-contents-center align-items-center">
              <router-link :to="{name : 'moviedetail', params:{moviePk : modalData.id}}">
                <button class="reviewbtn">댓글&평점 보러 가기</button>
              </router-link>
              <font-awesome-icon icon="fa-solid fa-heart" @click="likeMovie(modalData.id)" v-if="isLike"></font-awesome-icon>
              <font-awesome-icon icon="fa-regular fa-heart" @click="likeMovie(modalData.id)" v-if="!isLike"></font-awesome-icon>
            </div>
          </div>
          <div v-else>
            <p>아직 리뷰가 존재하지 않아요!</p>
            <div class="d-flex justify-contents-center align-items-center">
              <router-link :to="{name : 'moviedetail', params:{moviePk : modalData.id}}">
                <button class="reviewbtn">댓글&평점 달아주기</button>
              </router-link>
              <font-awesome-icon icon="fa-solid fa-heart" @click="likeMovie(modalData.id)" v-if="isLike"></font-awesome-icon>
              <font-awesome-icon icon="fa-regular fa-heart" @click="likeMovie(modalData.id)" v-if="!isLike"></font-awesome-icon>
            </div>
          </div>
        </div>
      </div>
    </b-modal>
    <b-pagination
      class="moviePaging"
      v-model="currentPage"
      pills
      :total-rows="rows"
      :per-page="perPage"
    ></b-pagination>
  </div>
</div>
</template>

<script>
import { Carousel, Slide } from 'vue-carousel';
import { mapActions} from 'vuex'
import moment from "moment"
import axios from 'axios'
import drf from '@/api/drf'
export default {
  name:'HomeView',
  data(){
    return {
      perPage:8,
      currentPage:1,
      modalData:null,
      isLike:false,
      movieRelease:null,
      slide:0,
      sliding:null
    }
  },
  components: {
    Carousel,
    Slide
  },
  computed:{
    Movies(){
      const movies = this.$store.getters.movies
      return movies.slice(
        (this.currentPage -1)*this.perPage,
        this.currentPage*this.perPage
      )
    },
    rows(){
      return this.$store.getters.movies.length
    }
  },
  methods:{
    ...mapActions(['fetchMovies', 'likeMovie', 'fetchCurrentUser']),
    openModal(data){
      this.modalData = data,
      this.checkLike(this.modalData.id)
      this.formatMovieRelease()
    },
    formatMovieRelease(){
      moment.locales('ko')
      const ReleaseDate = moment(this.modalData.release_date)
      const AfterRelease = ReleaseDate.format("YYYY년 M월 D일")
      this.movieRelease = AfterRelease
    },
    likeMovie(moviePk){
      axios({
        url:drf.movies.likeMovie(moviePk),
        method:'post',
        headers:this.$store.getters.authHeader
      })
        .then(res => {
          this.isLike = res.data.isLike
        })
        .catch(err => console.error(err.response))
    },
    checkLike(moviePk){
      axios({
        url:drf.movies.checkLike(moviePk),
        method:'get',
        headers:this.$store.getters.authHeader
      })
        .then(res => {
          this.isLike = res.data.isLike
        })
        .catch(err => console.error(err.response))
    }
  },
  created(){
    this.fetchMovies()
    this.fetchCurrentUser()
  }
}
</script>

<style>
.container{
  margin:20px auto;
  max-width: 1000px;
  width:80%;
  padding:10px;
  margin-bottom:35px;
}
.movieCard .card-body{
  padding:0;
}
.movieCard{
  margin-bottom:35px;
}
.movieCard:hover{
  transform: scale(1.05);
}
.movieCard img{
  border-radius:0.25rem;
}
.container h1{
  margin-bottom:50px;
}
.moviePaging{
  padding:0;
  display:flex;
  justify-content: center;
  margin:30px 0 20px 0;
}
li span, .moviePaging li button{
  color:tomato;
}
.moviePaging .page-item.active .page-link{
  background-color:tomato;
  border-color:tomato;
}
.moviePaging .page-link{
  border-color:tomato;
}
.moviePaging .page-link:hover{
  color:tomato;
}
#MovieModal .close{
  border: 0px;
  background-color: transparent;
  font-size:30px;
  margin-top:-10px;
  padding:0;
  color:tomato;
}
#MovieModal .modal-header{
  border-bottom: 0px;
  padding: 16px 16px 0 16px;
}
#MovieModal .modal-footer{
  border-top: 0px;
}
#MovieModal .modal-body .modalPoster{
  width:14rem;
}
#MovieModal .modal-title{
  margin-left:10px;
  font-weight:bold;
}
#MovieModal .modal-body{
  padding:0;
  margin:10px 30px 30px 30px;
}
#MovieModal{
  font-family: 'IBM Plex Sans KR';
  font-weight: 500;
}
.fa-heart{
  font-size:35px;
  color:tomato;
}
.fa-star{
  color:orange;
}
.modal-contents{
  display:flex;
}
.mgenre{
background-color: tomato;
color:white;
margin-right:10px;
padding:5px 10px;
border-radius: 5px;
}
.overview{
  padding:10px 15px;
  border-radius: 10px;
  box-shadow: 1px 1px 3px 1px #dadce0 inset;
  font-size:15px;
}
.reviewbtn{
  background-color: black;
  border:0px;
  border-radius: 10px;
  margin-right:15px;
  color:white;
  padding:10px 15px;
}
.category{
  font-size:18px;
  font-weight: bold;
}
.full-screen {
  width: 100vw;
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
}
.banner-img{
  width:80%;
}
.gotorecobtn{
  background-color: #262626;
  border:0px;
  border-radius: 10px;
  padding: 10px 15px;
  color:tomato;
  width:30%;
}
.gotoreco{
  position:relative;
  top:-10%;
}
</style>
