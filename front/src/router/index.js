import { createRouter, createWebHistory } from 'vue-router'
import Home from '@/pages/home/HomePage.vue'
import About from '@/pages/about/AboutPage.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/about',
    name: 'About',
    component: About
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
