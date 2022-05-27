<template>
  <div class="newOreditArticle">
    <h3 class="newOreditWord">글 수정</h3>
    <article-form v-if="isArticle" :article="article" actions="update"></article-form>
  </div>
</template>

<script>
import ArticleForm from '../components/ArticleForm.vue'
import {mapGetters, mapActions} from 'vuex'

export default {
  name:'ArticleEdit',
  components: { ArticleForm },
  computed:{
    ...mapGetters(['article', 'isArticle'])
  },
  methods:{
    ...mapActions(['fetchArticle'])
  },
  created(){
    this.fetchArticle(this.$route.params.articlePk)
  }
}
</script>

<style>

</style>