// import api from "@/api/rules.js"
// import {
//   message
// } from "ant-design-vue";
const state = {
  namespaced: true,
  state: {
    starSelectedKeys: [],//当前选定菜单
    collapsed: false,//是否收缩菜单 false展开 true 收缩
  },
  mutations: {
    setStarSelectedKeys (state, val) {
      localStorage.setItem('starSelectedKeys', val.toString());
      state.starSelectedKeys = [val]
    },
    setCollapsed (state, val) {
      state.collapsed = val
    }
  },
  actions: {


  },
  getters: {
    starSelectedKeys: (state) => {
      state.starSelectedKeys = [localStorage.getItem('starSelectedKeys')];
      return state.starSelectedKeys
    },
    collapsed: (state) => {
      return state.collapsed
    }
  }
}

export default state