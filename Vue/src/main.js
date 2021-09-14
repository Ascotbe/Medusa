import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import Antd from 'ant-design-vue';
import axios from 'axios'
import * as echarts from 'echarts';
// import 'ant-design-vue/dist/antd.css';
import 'ant-design-vue/dist/antd.less'
import api from './api/rules'
Vue.use(Antd)
Vue.prototype.$axios = axios
Vue.prototype.$api = api
Vue.prototype.$store = store
Vue.config.productionTip = false
Vue.prototype.$echarts = echarts

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
