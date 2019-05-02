import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home.vue'
import Account from '@/components/Account'
import Contact from '@/components/Contact.vue'
import Products from '@/components/Products.vue'
import Recipes from '@/components/Recipes.vue'
import ViewProduct from '@/components/ViewProduct.vue'

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
      path: '/account',
      name: 'Account',
      component: Account
    },
    {
      path: '/products',
      name: 'Products',
      component: Products
    },
    {
      path: '/recipes',
      name: 'Recipes',
      component: Recipes
    },
    {
      path: '/products/:id?',
      name: 'ViewProduct',
      component: ViewProduct
    }
  ]
})
