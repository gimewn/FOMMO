<template>
  <div>
    <movie-comment-form class="mb-5"/>
    <movie-comment-item v-for="comment in comments" :key="comment.pk" :comment="comment"/>
  </div>
</template>

<script>
import MovieCommentForm from './MovieCommentForm.vue'
import MovieCommentItem from './MovieCommentItem.vue'
export default {
  components: { MovieCommentForm, MovieCommentItem },
  props:{
    comments:Array
  }
}
</script>

<style>

</style>