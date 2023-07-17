import { createRouter, createWebHistory } from 'vue-router'
const home = () => import('@/pages/home/HomePage.vue')
const ServicesByCategoryPage = () => import('@/pages/services/byCategory/ServicesByCategoryPage.vue')
const userDetailesPage = () => import('@/pages/services/userByCategory/userByCategoryPage.vue')
const usersPage = () => import('@/pages/users/UsersPage.vue')
const editPage =() => import('@/pages/edit/editPage.vue')
const publishServicePage = () => import('@/pages/publishService/publishServicePage.vue')
// const requestPage = ()=> import('@/pages/users/requestPage.vue') 
const routes = [
  {
    path: '/',
    name: 'Home',
    component: home
  },
  {
    path: '/user/:id',
    name: 'usersPage',
    component: usersPage,
    props: true
  },
  {
    path: '/services/by-category/:category_id',
    name: 'ServicesByCategoryPage',
    component: ServicesByCategoryPage,
    props: true
  },
  {
    path: '/services/user_services/:id',
    name: 'userDetailesPage',
    component: userDetailesPage,
    props: true
  },
  {
    path: '/services/user_services/:id/:cat_id',
    name: 'editPage',
    component: editPage,
    props: true
  },
  {
    path: '/user_services/:id',
    name: 'publishServicePage',
    component: publishServicePage,
    props: true
  },
  // {
  //   path: '/request',
  //   name: 'requestPage',
  //   component: requestPage,
  // },
  
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
