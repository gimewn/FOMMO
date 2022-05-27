<template>
  <div>
    <h1 class="mb-1">Community</h1>
    <button>
      <router-link :to="{name:'articlecreate'}">새 글 작성</router-link>
    </button>
    <table>
      <thead width="500">
        <th>번호</th>
        <th>제목</th>
        <th>작성자</th>
      </thead>
      <tbody v-for="(article, index) in Articles" :key="article.pk">
        <tr>
          <td width="100">{{index+1}}</td>
          <td width="300"><router-link :to="{name : 'article', params:{articlePk : article.pk}}" class="articleTitle">{{article.title}}</router-link></td>
          <td width="100">{{article.user.username}}</td>
        </tr>
      </tbody>
    </table>
    <b-pagination
      class="moviePaging"
      v-model="currentPage"
      pills
      :total-rows="rows"
      :per-page="perPage"
    ></b-pagination>
  </div>
</template>

<script>
import {mapActions} from 'vuex'
export default {
  name:'ArticleList',
  data(){
    return {
      perPage:5,
      currentPage:1,
      fields:['번호', '제목', '작성자'],
      articles: this.$store.getters.articles
    }
  },
  computed:{
    Articles(){
      const articles = this.$store.getters.articles
      return articles.slice(
        (this.currentPage -1)*this.perPage,
        this.currentPage*this.perPage
      )
    },
    rows(){
      return this.$store.getters.articles.length
    }
  },
  methods:{
    ...mapActions(['fetchArticles']),
    AddIndex(){
      this.index = this.index+1
    }
  },
  created(){
    this.fetchArticles()
  }
}
</script>

<style scoped>
table {
  margin:0 auto 30px auto;
  width:100%;
}
.articleTitle{
  text-decoration: none;
  color:black;
}
.likeUsers{
  font-size:10px;
}
td {
  padding:10px;
}
tbody{
  border-bottom:1px solid black;
}
button{
  margin-left:500px;
  margin-bottom:25px;
  background-color:black;
  border:0;
  border-radius: 10px;
  padding:5px 10px;
}
button > a{
  text-decoration: none;
  color:white;
}
thead{
  border-bottom:2px solid tomato;
}
th{
  padding:10px;
}
h1{
  font-family: 'Alfa Slab One';
  color:tomato;
}
</style>