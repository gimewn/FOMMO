<template>
  <nav class="menu">
    <router-link  outer-link :to="{name:'Home'}">
      <div id='logo' class="d-flex">
        <h3 class="logoFomo">FO</h3>
        <h3 class="logoMovie">M</h3>
        <h3 class="logoFomo">MO</h3>
      </div>
    </router-link>
    <div v-if="!isLoggedIn" class="category">
      <span>
        <router-link :to="{name:'login'}">로그인</router-link>
      </span>
      <span>
        <router-link :to="{name:'signup'}">회원가입</router-link>
      </span>
    </div>
    <div v-if="isLoggedIn" class="category">
      <span>
        <router-link :to="{name:'Home'}">홈</router-link>
      </span>
      <span>
        <router-link :to="{name:'recoMovie'}">영화 추천</router-link>
      </span>
      <span>
        <router-link :to="{name:'articles'}">커뮤니티</router-link>
      </span>
      <span>
        <router-link :to="{name:'logout'}">로그아웃</router-link>
      </span>
    </div>
  </nav>
</template>

<script>
import { mapGetters } from 'vuex'
export default {
computed:{
  ...mapGetters(['isLoggedIn'])
},
}
</script>

<style>
.menu{
  display:flex;
  justify-content: space-between;
  padding:25px 35px;
  margin-bottom:30px;
}
.menu a{
  text-decoration: none;
  margin-right:10px;
  color:#2b2b2b;
}
.menu a:hover{
  color:tomato;
}
.category{
  display:flex;
  align-items: center;
}
.menu h3{
  margin:0;
  color:black;
}
#logo{
  font-family: 'Alfa Slab One';
}
#logo .logoMovie{
  color:#2b2b2b;
}
#logo .logoFomo{
  color:tomato;
}
</style>