import Vue from 'vue'
import Vuex from 'vuex'
let cart = localStorage.getItem('cart');
Vue.use(Vuex)

export default new Vuex.Store({
  state: {

    dark: {
      backgroundColor: "#3c3d3f",
      border: "none",
      color: "white",
    },
    darkmode: false,
    DisplayCheck: false,
    cart: cart ? JSON.parse(cart) : [],


  },
  mutations: {
    ChangeMode(state) {
      if (state.darkmode == true) {
        state.darkmode = false;
      } else {
        state.darkmode = true;
      }

    },
    addToCart(state, item) {
      state.cart.push(item);
      this.commit('saveCart');
    },
    saveCart(state) {
      localStorage.setItem('cart', JSON.stringify(state.cart));
    },
    DisplayCheck(state) {
      state.DisplayCheck = true;
    },
    DisplayAdd(state) {
      state.DisplayCheck = false;
    },
    removeFromCart(state, item) {
      let index = state.cart.indexOf(item);

      if (index > -1) {
        state.cart.splice(index, 1);
        state.cart.splice()
      }
      this.commit('saveCart');
    }

  }
})