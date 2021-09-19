import api from "@/api/rules.js"
import {
  message
} from "ant-design-vue";
const state = {
  namespaced: true,
  state: {
    verificationcodekey: '', //验证码key
    token: '',
    userinfo: {},

  },
  mutations: {
    setVerificationcodekey (state, val) {
      localStorage.setItem('verificationcodekey', val);
      state.verificationcodekey = val
    },
    setToken (state, val) {
      localStorage.setItem('token', val);
      state.token = val
    },
    setUserinfo (state, val) {
      state.userinfo = val
    }
  },
  actions: {
    async setUserinfo ({
      commit
    }, val) {
      const token = {
        token: val
      }
      await api.user_info(token).then((res) => {
        if (res.code == 200) {
          commit('setToken', val)
          commit('setUserinfo', res.message)
        } else {
          message.error(res.message)
          commit('setUserinfo', {})
        }
      })

    }
  },
  getters: {
    verificationcodekey: (state) => {
      state.verificationcodekey = localStorage.getItem('verificationcodekey');
      return state.verificationcodekey
    },
    token: (state) => {
      state.token = localStorage.getItem('token');
      return state.token
    },
    userinfo: (state) => {
      return state.userinfo
    },
  }
}

export default state