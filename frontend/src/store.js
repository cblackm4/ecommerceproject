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
        },
        cart: {
            recipes: [],
            products: []
        }
    },
  getters: {
      user: state => state.user,
      cart: state => state.cart,
  },
  mutations: {
    setUser(state, user) {
      state.user = user;
      },
      setCart(state, cart) {
          state.cart = cart;
      }
  },
  actions: {
    setUser(context, user) {
      context.commit('setUser', user);
      },
      setCart(context, cart) {
          context.commit('setCart', cart);
      }
  }
})
