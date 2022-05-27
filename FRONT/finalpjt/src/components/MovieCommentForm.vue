<template>
  <form @submit.prevent="onSubmit" class="reviewForm">
    <b-form-rating class="starRating" v-model="score" variant="warning" show-value show-value-max size="lg" no-border></b-form-rating>
    <div class="d-flex flex-row justify-content-center mt-4">
      <label for="comment"></label>
      <b-form-input v-model="content" id='text' placeholder="영화에 대한 의견을 남겨주세요!" type="text" required></b-form-input>
      <button class="mcommentsubmit">등록</button>
    </div>
  </form>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
export default {
  name:'MovieCommentForm',
  data(){
    return {
      score:0,
      content:'',
      moviePk: this.$route.params.moviePk,
    }
  },
  computed:{
    ...mapGetters(['movie'])
  },
  methods:{
    ...mapActions(['createMovieComment']),
    onSubmit(){
      const datas = {
        content:this.content,
        score:this.score
      }
      this.createMovieComment({moviePk:this.moviePk, datas:datas})
      this.content=''
      this.score = 0
    },
    ratingToPercent() {
      const score = +this.restaurant.averageScore * 20;
      return score + 1.5;
    }
  }
}
</script>

<style scoped>
#text{
  width:15rem;
}
form{
  margin: 20px auto;
  display: flex;
  justify-content: center;
  flex-direction: column;
}
.mcommentsubmit{
  margin-left:10px;
  background-color: tomato;
  border:0;
  border-radius: 5px;
  color:white;
  padding:5px 10px;
}
.starRating{
  width:30%;
  margin: 0 auto;
}
</style>