import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './Vuex'
import axios from 'axios'
import 'lib-flexible'
import VueCodemirror from 'vue-codemirror'
import "codemirror/mode/javascript/javascript.js"
import Antd from 'ant-design-vue'
import 'ant-design-vue/dist/antd.less' // or 'ant-design-vue/dist/antd.less'
import echarts from 'echarts'
import api from './api/rules'

import qj from './Js/QJfunction'//全局方法



// import base style
import 'codemirror/lib/codemirror.css'
import 'codemirror/theme/duotone-light.css'
// import more codemirror resource...

// you can set default global options and events when Vue.use
Vue.use(VueCodemirror, /* {
  options: { theme: 'base16-dark', ... },
  events: ['scroll', ...]
} */)
Vue.use(qj)

Vue.prototype.$echarts = echarts
Vue.prototype.$axios = axios
Vue.prototype.$api = api



Vue.use(Antd)

Vue.config.productionTip = false
new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
