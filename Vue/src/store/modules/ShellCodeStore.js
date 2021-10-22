const state = {
  namespaced: true,
  state: {
    trojanId: '',
    trojanGenerateFileName: '',
  },
  mutations: {
    setTrojanId (state, val) {
      state.trojanId = val
    },
    setTrojanGenerateFileName (state, val) {
      state.trojanGenerateFileName = val
    }
  },
  actions: {
    setTrojanId ({
      commit
    }, val) {
      commit('setTrojanId', val)
    },
    setTrojanGenerateFileName ({
      commit
    }, val) {
      commit('setTrojanGenerateFileName', val)
    },
  },
  getters: {
  }
}

export default state