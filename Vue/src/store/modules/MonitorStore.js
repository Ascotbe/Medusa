const state = {
  namespaced: true,
  state: {
    vulnerabilityCode: ''
  },
  mutations: {
    setVulnerabilityCode (state, val) {
      localStorage.setItem('vulnerabilityCode', val);
      state.vulnerabilityCode = val
    }
  },
  actions: {


  },
  getters: {
    vulnerabilityCode: (state) => {
      return state.vulnerabilityCode
    },
  }
}
export default state
