import { createRouter, createWebHistory } from 'vue-router'
import MainView from '@/views/MainView.vue'
import LoginView from '@/views/LoginView.vue'
import SignupView from '@/views/SignupView.vue'
import ProfileView from '@/views/ProfileView.vue'
import ProductView from '@/views/ProductView.vue'
import ProductDetailView from '@/views/ProductDetailView.vue'
import ExchangeView from '@/views/ExchangeView.vue'
import MapView from '@/views/MapView.vue'
import WelcomeView from '@/views/WelcomeView.vue'
import BoardsView from '@/views/BoardsView.vue'
import BoardsDetailView from '@/views/BoardsDetailView.vue'
import BoardsCreateView from '@/views/BoardsCreateView.vue'
import { accountStore } from '@/stores/accountStore'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'main',
      component: MainView
    },
    {
      path: '/login',
      name: 'login',
      component: LoginView,
      beforeEnter: ((to, from, next) => {
        const accStore = accountStore()
        if (accStore.isLogin) {
          window.alert('로그인 되어있습니다.')
          next(from)
        } else {
          next()
        }
      })
    },
    {
      path: '/signup',
      name: 'signup',
      component: SignupView,
      beforeEnter: ((to, from, next) => {
        const accStore = accountStore()
        console.log(accStore.isLogin)
        if (accStore.isLogin) {
          window.alert('로그인 되어있습니다.')
          next(from)
        } else {
          next()
        }
      })
    },
    {
      path: '/profile/:username',
      name: 'profile',
      component: ProfileView,
    },
    {
      path: '/product',
      name: 'product',
      component: ProductView
    },
    {
      path: '/product/:type/:pk',
      name: 'productDetail',
      component: ProductDetailView
    },
    {
      path: '/exchange',
      name: 'exchange',
      component: ExchangeView
    },
    {
      path: '/map',
      name: 'map',
      component: MapView
    },
    {
      path: '/welcome',
      name: 'welcome',
      component: WelcomeView
    },
    {
      path: '/boards/',
      name: 'boards',
      component: BoardsView
    },
    {
      path: '/boards/:pk',
      name: 'boardsDetail',
      component: BoardsDetailView
    },
    {
      path: '/boards/create',
      name: 'boardsCreate',
      component: BoardsCreateView,
      beforeEnter: ((to, from, next) => {
        const accStore = accountStore()
        if (!accStore.isLogin) {
          window.alert('로그인이 필요한 서비스입니다.')
          next(from)
        } else {
          next()
        }
      })
    },
  ]
})

export default router
