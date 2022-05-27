<template>
  <div>
    <article-comment-form/>
    <article-comment-list-item v-for="comment in comments" :key="comment.pk" :comment="comment"></article-comment-list-item>
  </div>
</template>

<script>
import ArticleCommentForm from './ArticleCommentForm.vue'
import ArticleCommentListItem from './ArticleCommentListItem.vue'
export default {
  components: { ArticleCommentForm, ArticleCommentListItem },
  props:{
    comments:Array
  }
}
</script>

<style>

</style>