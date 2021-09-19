// import api from "@/api/rules.js"
// import {
//   message
// } from "ant-design-vue";
const state = {
  namespaced: true,
  state: {
    starSelectedKeys: []
  },
  mutations: {
    setStarSelectedKeys (state, val) {
      localStorage.setItem('starSelectedKeys', val.toString());
      state.starSelectedKeys = [val]
    }
  },
  actions: {


  },
  getters: {
    starSelectedKeys: (state) => {
      state.starSelectedKeys = [localStorage.getItem('starSelectedKeys')];
      return state.starSelectedKeys
    },
  }
}

export default state