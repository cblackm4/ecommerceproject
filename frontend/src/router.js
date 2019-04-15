import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home.vue'
import Account from '@/components/Account'
import Contact from '@/components/Contact.vue'
import Signup from '@/components/Signup'
import Login from '@/components/Login'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/contact',
      name: 'Contact',
      component: Contact
    },
    {
      path: '/signup',
      name: 'Signup',
      component: Signup
    },
    {
      path: '/login',
      name: 'Login',
      component: Login
    },
    {
      path: '/account',
      name: 'Account',
      component: Account
    }
  ]
})
