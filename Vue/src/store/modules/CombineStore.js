const state = {
  namespaced: true,
  state: {
    markdown_name: '',//协同文档名称
    markdown_project_name: '',//协同项目名
    comparisonData: {},//比较数据（new 新数据，old 原有数据）
  },
  mutations: {
    setMarkdown_name (state, val) {
      state.markdown_name = val
    },
    setMarkdown_project_name (state, val) {
      state.markdown_project_name = val
    },
    setComparisonData (state, val) {
      state.comparisonData = val
    }

  },
  actions: {
    setMarkdown_name ({ commit }, val) {
      commit('setMarkdown_name', val)
    },
    setMarkdown_project_name ({ commit }, val) {
      commit('setMarkdown_project_name', val)
    },
    setComparisonData ({ commit }, val) {
      commit('setComparisonData', val)
    }
  },
  getters: {
    markdown_name: (state) => {
      return state.markdown_name
    },
    markdown_project_name: (state) => {
      return state.markdown_project_name
    },
    comparisonData: (state) => {
      return state.comparisonData
    }
  }
}
export default state
