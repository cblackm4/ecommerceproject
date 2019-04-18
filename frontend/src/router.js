import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home.vue'
import Account from '@/components/Account'
import Contact from '@/components/Contact.vue'
import Signup from '@/components/Signup'
import Login from '@/components/Login'

Vue.use(Router)

export default new Router({
  /* To add a new page, import the component from '/@components/***' then add the following
  * route information
  * Path: path to be displayed in the $.browser.
  * Name: name of the component
  * Component: the component
  */
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
