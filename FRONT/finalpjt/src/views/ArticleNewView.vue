<template>
  <div class="newOreditArticle">
    <h3 class="newOreditWord">새 글 작성</h3>
    <article-form :article="article" actions="create"></article-form>
  </div>
</template>

<script>
import ArticleForm from '../components/ArticleForm.vue'
export default {
  name:'NewArticle',
  components:{
    ArticleForm
  },
  data(){
    return{
      article:{
        pk:null,
        title:'',
        content:''
      }
    }
  }
}
</script>

<style>
.newOreditArticle{
  box-shadow: 1px 1px 3px 1px #dadce0 inset;
  border-radius:30px;
  padding:30px 40px 30px 30px;
  width:500px;
  min-width:300px;
  margin:0 20px;
}
.newOreditWord{
  color:black;
}
</style>