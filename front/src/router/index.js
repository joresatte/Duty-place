import { createRouter, createWebHistory } from 'vue-router'
import home from '@/pages/home/homePage.vue'
import contactdetails from '@/pages/contactdetails/contactDetailsPage.vue'
import contactsPage from '@/pages/contacts/contactsPage.vue'
import addNewContact  from '@/pages/newContact/newContactAddingPage.vue'


const routes = [
  {
    path: '/',
    name: 'home',
    component: home
  },
  {
    path: '/contact/:id',
    name: 'contactdetails',
    component: contactdetails,
    props: true
  },
  {
    path: '/contact/add',
    name: 'addNewContact',
    component: addNewContact
  },
  {
    path: '/contact',
    name: 'contactsPage',
    component: contactsPage
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
})

export default router
