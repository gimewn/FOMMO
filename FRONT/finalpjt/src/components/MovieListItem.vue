<template>
  <div>
    <b-card
    :img-src="Poster"
    img-alt="Image"
    img-top
    tag="article"
    style="max-width: 20rem;"
    class="mb-2"
  >
  </b-card>
  
  </div>
</template>

<script>
import { mapActions } from 'vuex'
export default {
  name:'MovieListItem',
  props:{
    movie:Object
  },
  data(){
    return{
      Poster:`https://www.themoviedb.org/t/p/w600_and_h900_bestv2/${this.movie.poster_url}`,
      visible:false,
    }
  },
  methods:{
    ...mapActions(['likeMovie']),
    showModal(){
      this.visible = !this.visible;
      console.log(this.visible)
    }
  },
}
</script>

<style>

</style>