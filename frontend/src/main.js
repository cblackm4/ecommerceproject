import Vue from 'vue'
import './plugins/vuetify'
import App from './App.vue'
import store from './store'
import router from './router'
import axios from 'axios'
import VueCookies from 'vue-cookies'

Vue.prototype.$axios = axios;
Vue.prototype.$cookies = VueCookies;

Vue.config.productionTip = false

new Vue({
  store,
  router,
  render: h => h(App)
}).$mount('#app')
