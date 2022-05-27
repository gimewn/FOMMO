<template>
  <div>
    <form @submit.prevent="onSubmit">
      <div class="d-flex align-items-center titleinput">
        <label for="title" class="me-2">제목</label>
        <b-form-input type="text" id="title" v-model="newArticle.title" placeholder="글의 제목을 입력해주세요."></b-form-input>
      </div>
      <div class="d-flex align-items-center">
        <label for="content" class="me-2">내용</label>
        <b-form-textarea type="text" id="content" v-model="newArticle.content" placeholder="글의 내용을 입력해주세요."></b-form-textarea>
      </div>
      <div>
        <button v-if="actions === 'create'">등록</button>
        <button v-if="actions === 'update'">수정</button>
      </div>
    </form>
  </div>
</template>
<script>
import {mapActions} from 'vuex'
export default {
  name:'ArticleForm',
  props:{
    article:{
      Object
    },
    actions:{
      String
    }
  },
  data(){
    return{
      newArticle:{
        title:this.article.title,
        content:this.article.content
      },
      articlePk: this.$route.params.articlePk
    }
  },
  methods:{
    ...mapActions(['createArticle', 'editArticle']),
    onSubmit(){
      if(this.actions==="create"){
        this.createArticle(this.newArticle)
      }else if (this.actions === 'update'){
        const payload = {
          articlePk:this.articlePk,
          ...this.newArticle
        }
        this.editArticle(payload)
      }
    }
  }
}
</script>

<style scoped>
#title, #content{
  max-width:500px;
  width:300%;
}
textarea{
  height:200px;
}
label{
  width:50%;
  color:tomato;
  font-weight: bold;
}
.titleinput{
  margin:30px 0;
}
button{
  margin-top:20px;
  background-color: tomato;
  color:white;
  font-weight: bold;
  padding:10px 15px;
  border-radius:10px;
  border:0;
  width:8rem;
}
</style>