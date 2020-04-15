import Splitpane from './split-pane/index.vue'

export default Splitpane

if (typeof window !== 'undefined' && window.Vue) {
  window.Vue.component('split-pane', Splitpane)
}
