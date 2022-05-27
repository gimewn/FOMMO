import router from '@/router'
import axios from 'axios'
import drf from '@/api/drf'

import _ from 'lodash'

export default {
  state: {
    articles:[],
    article:{},
  },
  getters: {
    articles : state => state.articles,
    article: state => state.article,
    isAuthor: (state, getters) => {
      return state.article.user?.username === getters.currentUser.username
    },
    isArticle: state => !_.isEmpty(state.article),
  },
  mutations: {
    SET_ARTICLES : (state, articles) => state.articles = articles,
    SET_ARTICLE : (state, article) => state.article = article,
    SET_ARTICLE_COMMENTS : (state, comments) => (state.article.article_comments = comments)
  },
  actions: {
    fetchArticles({commit, getters}){
      axios({
        url: drf.articles.articles(),
        method:'get',
        headers: getters.authHeader
      })
        .then(res => commit('SET_ARTICLES', res.data))
        .catch(err => console.error(err.response))
    },
    fetchArticle({commit, getters}, articlePk){
      axios({
        url:drf.articles.article(articlePk),
        method:'get',
        headers: getters.authHeader
      })
        .then(res => {
          commit('SET_ARTICLE', res.data)
        })
        .catch(err => {
          console.error(err.response.data)
          if(err.response.status === 404){
            router.push({name:'NotFound404'})
          }
        })
    },
    createArticle({commit, getters}, article){
      axios({
        url:drf.articles.createArticle(),
        method:'post',
        data:article,
        headers:getters.authHeader
      })
        .then(res => {
          commit('SET_ARTICLE', res.data)
          router.push({
            name:'article',
            params:{articlePk:getters.article.pk}
          })
        })
        .catch(err => console.error(err.response))
    },
    editArticle({commit, getters}, {articlePk, title, content}){
      axios({
        url:drf.articles.editArticle(articlePk),
        method:'put',
        data:{title, content},
        headers:getters.authHeader
      })
        .then(res => {
          commit('SET_ARTICLE', res.data)
          router.push({
            name:'article',
            params:{articlePk:getters.article.pk}
          })
        })
        .catch(err => console.error(err.response))
    },
    deleteArticle({commit, getters}, articlePk){
      if (confirm('정말 삭제하시겠습니까?')){
        axios({
          url:drf.articles.deleteArticle(articlePk),
          method:'delete',
          headers:getters.authHeader
        })
          .then(()=>{
            commit('SET_ARTICLE', {})
            router.push({name:'articles'})
          })
          .catch(err => console.error(err.response))
      }
    },
    likeArticle({commit, getters}, articlePk){
      axios({
        url:drf.articles.likeArticle(articlePk),
        method:'post',
        headers:getters.authHeader
      })
        .then(res => commit('SET_ARTICLE', res.data))
        .catch(err => console.error(err.response))
    },
    createArticleComment({commit, getters}, {articlePk, content}){
      const comment = {content}
      axios({
        url:drf.articles.createArticleComment(articlePk),
        method:'post',
        data:comment,
        headers: getters.authHeader
      })
        .then(res => commit('SET_ARTICLE_COMMENTS', res.data))
        .catch(err => console.error(err.response))
    },
    editArticleComment({commit, getters}, {articlePk, commentPk, content}){
      axios({
        url:drf.articles.editArticleComment(articlePk, commentPk),
        method:'put',
        data:content,
        headers:getters.authHeader
      })
        .then(res => commit('SET_ARTICLE_COMMENTS', res.data))
        .catch(err => console.error(err.response))
    },
    deleteArticleComment({commit, getters}, {articlePk, commentPk}){
      axios({
        url:drf.articles.deleteArticleComment(articlePk, commentPk),
        method:'delete',
        data:{},
        headers:getters.authHeader
      })
        .then(res => commit('SET_ARTICLE_COMMENTS', res.data))
        .catch(err => console.error(err.response))
    }
  },
  modules: {
  }
}
