<template>
  <div class="comment">
    <span v-if="!isEditing" class="username">{{comment.user.username}}</span>
    <span v-if="!isEditing">
        <font-awesome-icon icon="fa-solid fa-star me-2"></font-awesome-icon>
        <span class="starScore ms-1">{{comment.score}}</span>
    </span>
    <span v-if="!isEditing">{{comment.content}}</span>
    <span v-if="isEditing">
      <b-form-input type="text" v-model="payload.content" class="editcontent mb-3"></b-form-input>
      <b-form-rating v-model="payload.score" class="starRating" variant="warning" no-border></b-form-rating>
      <button @click="onUpdate">수정</button>
      <button @click="switchIsEditing" class="canclebtn">취소</button>
    </span>
    <span v-if="currentUser.username === comment.user.username && !isEditing">
      <button @click="switchIsEditing">수정</button>
      <button @click="deleteMovieComment(payload)" class="deletebtn">삭제</button>
    </span>
  </div>
</template>

<script>
import {mapGetters, mapActions} from 'vuex'

export default {
  name:'MovieCommentListItem',
  props:{
    comment:Object
  },
  data(){
    return {
      isEditing:false,
      payload:{
        moviePk:this.comment.movie,
        commentPk:this.comment.id,
        content:this.comment.content,
        score:this.comment.score
      }
    }
  },
  computed:{
    ...mapGetters(['currentUser'])
  },
  methods:{
    ...mapActions(['editMovieComment', 'deleteMovieComment', 'fetchCurrentUser']),
    switchIsEditing(){
      this.isEditing = !this.isEditing
    },
    onUpdate(){
      this.editMovieComment(this.payload)
      this.isEditing = false
    }
  },
  created(){
    this.fetchCurrentUser()
  }
}
</script>

<style scoped>
button {
  background-color: tomato;
  color:white;
  border-radius: 5px;
  border: 0;
  padding: 5px 10px;
  font-size:12px;
}
.comment{
  display: flex;
  box-shadow: 1px 1px 3px 1px #dadce0 inset;
  padding:20px;
  width:50%;
  min-width:500px;
  margin: 20px auto;
  border-radius: 20px;
  align-items: center;
  justify-content: center;
}
span {
  margin-left:10px;
}
.starScore{
  margin:0;
}
.deletebtn, .canclebtn{
  margin-left:10px;
}
.username{
  font-weight:bold;
}
.starRating{
  width:50%;
  margin:0 auto 10px auto;
}

</style>