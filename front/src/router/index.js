import { createRouter, createWebHistory } from 'vue-router'
import Home from '@/pages/home/HomePage.vue'
import ServicesByCategoryPage from '@/pages/services/byCategory/ServicesByCategoryPage.vue'
import userDetailesPage from '@/pages/services/userByCategory/userByCategoryPage.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/services/by-category/:category_id',
    name: 'ServicesByCategoryPage',
    component: ServicesByCategoryPage,
    props: true
  },
  {
    path: '/services/by-category/:category_id/:id',
    name: 'userDetailesPage',
    component: userDetailesPage,
    props: true
  },
  
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
