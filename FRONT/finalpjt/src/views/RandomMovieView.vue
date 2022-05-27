<template>
  <div>
    <h1>Recommendation</h1>
    <!-- <h1>영화를 추천해드려요!</h1> -->
    <button @click="isreco=true, fetchRecoMovie()">FOMMO에게 영화 추천 받기</button>
    <div v-if="isreco">
      <div v-if="reco_movie.is_userlike" class="recoHeader">
        <h4><span class="username">{{reco_movie.user}}</span>님의 취향저격 장르는 </h4>
        <h2><span class="genrebr">{</span> <span class="recoGenre">{{reco_movie.genre_name}}</span> <span class="genrebr">}</span></h2>
        <h5>{{reco_movie.genre_name}} 장르의 이런 영화 어떠세요?</h5>
      </div>
      <div v-if="!reco_movie.is_userlike" class="recoHeader">
        <h3>{{reco_movie.user}}님, 아직 좋아요한 영화가 없으시네요!</h3>
        <h5>이런 영화는 어떠세요?</h5>
      </div>
      <div>
        <router-link :to="{name : 'moviedetail', params:{moviePk : reco_movie.movie.id}}">
          <span class="recomTitle">{{reco_movie.movie.title}}</span>
        </router-link>
        <div>
          <router-link :to="{name : 'moviedetail', params:{moviePk : reco_movie.movie.id}}">
            <img :src="`https://www.themoviedb.org/t/p/w600_and_h900_bestv2/${reco_movie.movie.poster_url}`" alt="" class="recoPoster">
          </router-link>
        </div>
      </div>
      <div v-if="!reco_movie.is_userlike">
        <p>좋아요 누르고 내 취향저격 영화 추천 받기</p>
        <button>
          <router-link :to="{name:'Home'}">좋아요 누르러 가기</router-link>
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
export default {
  data(){
    return{
      isreco:false
    }
  },
  methods:{
    ...mapActions(['fetchRecoMovie']),
  },
  computed:{
    ...mapGetters(['reco_movie'])
  },
}
</script>

<style scoped>
.recoHeader *{
  margin-bottom:30px;
}
h1{
  margin-bottom:30px;
}
.recoGenre{
  color:tomato;
}
.genrebr{
  color:black;
}
.username{
  /* color:tomato; */
  font-weight: bold;
}
.recoPoster{
  width:70%;
  border-radius: 10px;
  box-shadow: 1px 1px 3px 1px #dadce0 inset;
  margin: 30px 0;
}
button{
  background-color: black;
  border: 0px;
  border-radius: 10px;
  margin: 20px 0 50px 0;
  padding:10px 15px;
  color:white;
}
h1{
  font-family: 'Alfa Slab One';
  color:tomato;
  margin-bottom:50px;
}
.recomTitle{
  font-size:30px;
  font-weight:500;
  background-image: linear-gradient(120deg, orange 0%, tomato 100%);
  background-repeat: no-repeat;
  background-size: 100% 30%;
  background-position: 0 88%;
  transition: background-size 0.25s ease-in;
  padding:5px 10px;
  color:#2b2b2b;
}
.recomTitle:hover{
  background-size: 100% 88%;
  color:white;
}
a{
  text-decoration: none;
  color:white;
}
a:hover{
  color:tomato;
}
</style>