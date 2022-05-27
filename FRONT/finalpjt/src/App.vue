<template>
  <div id="fommo">
    <nav-bar></nav-bar>
    <div id="app">
      <router-view/>
    </div>
  </div>
</template>

<script>
import NavBar from '@/components/NavBar.vue'
import { mapActions } from 'vuex'

export default {
  name:'App',
  components:{
    NavBar
  },
  methods:{
    ...mapActions(['fetchCurrentUser'])
  },
  created(){
    this.fetchCurrentUser()
  }
}
</script>

<style>
#app {
  font-family: 'IBM Plex Sans KR', Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2b2b2b;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2b2b2b;
}

nav a.router-link-exact-active {
  color: tomato;
}
#fommo{
  font-family: 'IBM Plex Sans KR';
}
</style>
