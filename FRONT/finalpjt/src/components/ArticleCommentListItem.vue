<template>
  <div class="commentItem">
    <span class="commentuser">{{comment.user.username}}</span>
    <span v-if="!isEditing">{{payload.content}}</span>
    <span v-if="isEditing">
      <input type="text" v-model="payload.content">
      <button @click="onUpdate">수정</button>
      <button @click="switchIsEditing">취소</button>
    </span>
    <span v-if="currentUser.username === comment.user.username && !isEditing">
      <button @click="switchIsEditing">수정</button>
      <button @click="deleteArticleComment(payload)">삭제</button>
    </span>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
export default {
  name:'ArticleCommentListItem',
  props:{
    comment:Object
  },
  data(){
    return {
      isEditing:false,
      payload:{
        articlePk:this.comment.article,
        commentPk:this.comment.pk,
        content:this.comment.content
      }
    }
  },
  computed:{
    ...mapGetters(['currentUser'])
  },
  methods:{
    ...mapActions(['editArticleComment', 'deleteArticleComment', 'fetchCurrentUser']),
    switchIsEditing(){
      this.isEditing = !this.isEditing
    },
    onUpdate(){
      this.editArticleComment(this.payload)
      this.isEditing = false
    }
  },
  created(){
    this.fetchCurrentUser()
  }
}
</script>

<style scoped>
  .commentItem{
    box-shadow: 1px 1px 3px 1px #dadce0 inset;
    padding:20px;
    width:100%;
    min-width:300px;
    margin: 20px auto;
    border-radius: 20px;
}
.commentuser{
  font-weight:bold;
  margin-right:10px
}
button {
  background-color: tomato;
  color:white;
  border-radius: 5px;
  border: 0;
  padding: 5px 10px;
  margin-left:10px;
  font-size:1
  px;
}
</style>