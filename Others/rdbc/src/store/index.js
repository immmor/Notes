import { createStore } from 'vuex'

export default createStore({
  state: {
    token: localStorage.getItem('token') || '',
    role: localStorage.getItem('role') || ''
  },
  getters: {
  },
  mutations: {
    login(state, {token, role}){
      state.token = token;
      state.role = role;
      localStorage.setItem('token', token);
      localStorage.setItem('role', role);
    }
  },
  actions: {
  },
  modules: {
  }
})
