import Vue from 'vue'
import VueRouter from 'vue-router'
import store from '@/store'

import LoginView from '@/views/LoginView.vue'
import LogoutView from '@/views/LogoutView.vue'
import SignupView from '@/views/SignupView.vue'

import ArticleListView from '@/views/ArticleListView.vue'
import ArticleDetailView from '@/views/ArticleDetailView.vue'
import ArticleNewView from '@/views/ArticleNewView.vue'
import ArticleEditView from '@/views/ArticleEditView.vue'

import HomeView from '@/views/HomeView.vue'
import MovieDetailView from '@/views/MovieDetailView.vue'
import RandomMovieView from '@/views/RandomMovieView.vue'

import NotFound404View from '@/views/NotFound404View.vue'

Vue.use(VueRouter)

const routes = [
  {
    path:'/login',
    name:'login',
    component:LoginView
  },
  {
    path:'/logout',
    name:'logout',
    component:LogoutView
  },
  {
    path:'/signup',
    name:'signup',
    component:SignupView
  },
  {
    path: '/',
    name:'Home',
    component:HomeView
  },
  {
    path:'/movies/:moviePk',
    name:'moviedetail',
    component:MovieDetailView
  },
  {
    path:'/community',
    name:'articles',
    component:ArticleListView
  },
  {
    path:'/community/new',
    name:'articlecreate',
    component:ArticleNewView
  },
  {
    path:'/community/:articlePk',
    name:'article',
    component:ArticleDetailView
  },
  {
    path:'/community/:articlePk/edit',
    name:'articleedit',
    component:ArticleEditView
  },
  {
    path:'/recommendation',
    name:'recoMovie',
    component:RandomMovieView
  },
  {
    path:'/404',
    name:'NotFound404',
    component:NotFound404View
  },
  {
    path:'*',
    redirect:'/404'
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

router.beforeEach((to, from, next) => {
  store.commit('SET_AUTH_ERROR', null)
  const {isLoggedIn} = store.getters
  const noAuthPages = ['login', 'signup']
  const isAuthRequired = !noAuthPages.includes(to.name)

  if (isAuthRequired && !isLoggedIn) {
    alert('로그인 해주세요')
    next({ name: 'login' })
  } else {
    next()
  }
  if (!isAuthRequired && isLoggedIn) {
    next({ name: 'movies' })
  }
})



export default router
