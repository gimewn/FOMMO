<template>
  <form @submit.prevent="onSubmit">
    <label for="comment" >댓글</label>
    <b-form-input  type="text" id="comment" v-model="content" placeholder="댓글 내용을 입력해주세요" required></b-form-input>
    <button>등록</button>
  </form>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
export default {
  name:'ArticleCommentForm',
  data(){
    return {
      content:''
    }
  },
  computed:{
    ...mapGetters(['article'])
  },
  methods:{
    ...mapActions(['createArticleComment']),
    onSubmit(){
      this.createArticleComment({articlePk:this.article.pk, content:this.content })
      this.content=''
    }
  }
}
</script>

<style scoped>
#comment{
  width:50%;
}
form {
  margin: 20px auto;
  display: flex;
  justify-content: center;
  align-items: center;
}
button{
  margin-left:10px;
  background-color: tomato;
  border:0;
  border-radius: 5px;
  color:white;
  padding:5px 10px;
}
label {
  margin-right:10px;
}
</style>