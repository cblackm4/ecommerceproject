import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    user: {
      username: '',
      first_name: '',
      last_name: '',
      email: '',
      is_staff: false,
    }
  },
  getters: {
    user: state => state.user,
  },
  mutations: {
    setUser(state, user) {
      state.user = user;
    }
  },
  actions: {
    setUser(context, user) {
      context.commit('setUser', user);
    }
  }
})
