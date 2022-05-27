<template>
  <div>
    <h1>Logout</h1>
  </div>
</template>

<script>
import {mapGetters, mapActions} from 'vuex'

export default {
  name:'logoutView',
  methods:{
    ...mapActions(['logout'])
  },
  computed:{
    ...mapGetters(['isLoggedIn'])
  },
  created(){
    if(this.isLoggedIn){
      this.logout()
    }else{
      alert('로그인 해주세요.')
      this.$router.back()
    }
  }
}
</script>

<style>

</style>