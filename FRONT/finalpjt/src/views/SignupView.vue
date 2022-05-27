<template>
  <div class="signup">
    <h1 class="SingupTitle">SignUp</h1>
    <account-error v-if="authError"></account-error>
    <form @submit.prevent="signup(credentials)" class="signupForm">
      <div class="signupid">
        <label for="username"><p>아이디</p></label>
        <b-form-input v-model="credentials.username" id='username' placeholder="ID" type="text" required></b-form-input>
      </div>
      <div class="signupps1">
        <label for="password1"><p>비밀번호</p></label>
        <b-form-input v-model="credentials.password1" id='password1' placeholder="password" type="password" required></b-form-input>
      </div>
      <div class="signupps2">
        <label for="password2"><p>비밀번호 확인</p></label>
        <b-form-input v-model="credentials.password2" id='password2' placeholder="password confirmation" type="password" required></b-form-input>
      </div>
      <button class="signupbtn">회원가입</button>
    </form>
  </div>
</template>

<script>
import AccountError from '../components/AccountError.vue'
import {mapGetters, mapActions} from 'vuex'

export default {
  name:'signUp',
  components:{
  AccountError
  },
  data(){
    return{
      credentials:{
        username:'',
        password1:'',
        password2:''
      }
    }
  },
  computed:{
    ...mapGetters(['authError'])
  },
  methods:{
    ...mapActions(['signup'])
  }
}
</script>

<style>

</style>