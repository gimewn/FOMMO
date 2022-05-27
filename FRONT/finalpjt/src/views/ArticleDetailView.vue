<template>
  <div class="ArticleDetail">
    <div class="d-flex justify-contents-start">
      <h2>{{article.title}}</h2>
    </div>
    <div class="articleHeader">
      <div>
        <span class="writer me-2">
          {{article.user.username}}
        </span>
        <span>
          {{createDate}}
        </span>
      </div>
      <div v-if="currentUser.username === article.user.username">
        <router-link :to="{name:'articleedit', params:{articlePk}}">
          <button v-if="isAuthor" class="editbtn">수정</button>
          </router-link>
        <button @click="deleteArticle(articlePk)" class="deletebtn">
          삭제
        </button>
      </div>
    </div>
    <hr>
    <div>
      {{article.content}}
    </div>
    <div class="footer">
      <font-awesome-icon icon="fa-solid fa-heart" @click="likeArticle(articlePk)" style="font-size:15px; margin-right:5px;"></font-awesome-icon>
      <span class="me-2">{{likeCount}}</span>
      <span>댓글 {{commentCount}}</span>
    </div>
    <hr>
    <article-comment-list :comments="article.article_comments"/>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
import ArticleCommentList from '../components/ArticleCommentList.vue'
import moment from "moment"

export default {
  name:'ArticleDetail',
  components:{
    ArticleCommentList
  },
  data(){
    return{
      articlePk: this.$route.params.articlePk,
      createDate: null
    }
  },
  computed:{
    ...mapGetters(['isAuthor', 'article', 'currentUser']),
    likeCount(){
      return this.article.like_users?.length
    },
    commentCount(){
      return this.article.article_comments?.length
    }
  },
  methods:{
    ...mapActions(['fetchArticle', 'likeArticle', 'deleteArticle', 'fetchCurrentUser']),
  formatMovieRelease(){
    moment.locales('ko')
    const ReleaseDate = moment(this.article.created_at)
    const AfterRelease = ReleaseDate.format("YYYY-MM-DD HH:mm:ss")
    this.createDate = AfterRelease
    },
  },
  created(){
    this.fetchCurrentUser()
    this.fetchArticle(this.articlePk)
    this.formatMovieRelease()
  }
}
</script>

<style scoped>
.editbtn, .deletebtn{
  margin:10px 0 10px 10px;
  background-color:#2b2b2b;
  border:0;
  border-radius: 10px;
  padding:5px 10px;
  color:white;
  font-size:12px;
}
.writer{
  font-weight:bold;
}
.footer{
  display:flex;
  justify-content: flex-end;
  align-items: center;
}
.ArticleDetail{
  width:500px;
}
.articleHeader{
  display:flex;
  justify-content: space-between;
  align-items: center;
}
</style>