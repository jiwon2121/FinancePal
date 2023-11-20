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
      component: LoginView
    },
    {
      path: '/signup',
      name: 'signup',
      component: SignupView
    },
    {
      path: '/profile/:username',
      name: 'profile',
      component: ProfileView
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
  ]
})

export default router
