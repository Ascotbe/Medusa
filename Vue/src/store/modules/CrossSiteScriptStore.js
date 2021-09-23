const state = {
  namespaced: true,
  state: {
    projectAssociatedFileName: '',//跨站脚本钓鱼项目文件名字
  },
  mutations: {
    setProjectAssociatedFileName (state, val) {
      state.projectAssociatedFileName = val
    },
  },
  actions: {
    setProjectAssociatedFileName ({ commit }, val) {
      commit('setProjectAssociatedFileName', val)
    },
  },
  getters: {
    projectAssociatedFileName: (state) => {
      return state.projectAssociatedFileName
    },

  }
}
export default state
