<template>
  <div class="login">
    <h1 class="LoginTitle">Login</h1>
    <account-error v-if="authError"></account-error>
    <form @submit.prevent="login(credentials)" class="loginForm">
      <div class="idgroup">
        <label for="username"><p>아이디</p></label>
        <b-form-input v-model="credentials.username" id='username' placeholder="ID" type="text" required></b-form-input>
      </div>
      <div class="passwordgroup">
        <label for="password"><p>비밀번호</p></label>
        <b-form-input v-model="credentials.password" id='password' placeholder="Password" type="password" required></b-form-input>
      </div>
      <div class="mt-3">
        <button class="loginbtn me-3">로그인</button>
        <router-link :to="{name:'signup'}"><button class="signupbtn">회원가입</button></router-link>
      </div>
    </form>
  </div>
</template>

<script>
import AccountError from '../components/AccountError.vue'
import {mapGetters, mapActions} from 'vuex'

export default {
  name:'loginView',
  components:{
    AccountError
  },
  data(){
    return{
      credentials:{
        username:'',
        password:''
      }
    }
  },
  computed:{
    ...mapGetters(['authError'])
  },
  methods:{
    ...mapActions(['login'])
  },
}
</script>

<style>
  .login h1, .signup h1{
    margin-bottom:35px;
  }
  .login, .signup{
    display:flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    box-shadow: 1px 1px 3px 1px #dadce0 inset;
    padding:80px 90px 80px 80px;
    border-radius: 20px;
  }
  #username, #password, #password1, #password2{
    border:2px solid tomato;
    border-radius:10px;
    padding:10px;
  }
  #username:hover, #password:hover, #password1:hover, #password2:hover{
    background-color: white;
  }
  .idgroup, .signupid {
    display:flex;
    margin-top:10px;
    margin-bottom:30px;
    /* background-color: tomato;
    padding: 30px 30px 30px 20px; */
    border-radius: 35px;
  }
  .passwordgroup, .signupps1, .signupps2{
    display:flex;
    margin-bottom:35px;
    /* background-color: tomato;
    padding: 30px 30px 30px 20px; */
    border-radius: 35px;
  }
  .signupps2{
    margin-bottom:50px;
  }
  .idgroup p, .passwordgroup p, .signupid p, .signupps1 p, .signupps2 p{
    margin:0;
    color:tomato;
    font-weight: bold;
  }
  .idgroup label, .passwordgroup label, .signupid label, .signupps1 label, .signupps2 label{
    margin: auto 10px auto 0;
    width:50%;
  }
  .loginForm, .signupForm{
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
  }
  .loginbtn, .signupbtn {
    background-color: tomato;
    padding:10px 20px;
    color:white;
    font-weight:bold;
    border: 0px;
    border-radius:30px;
  }
  .LoginTitle, .SingupTitle{
    font-family: 'Alfa Slab One';
  }
</style>