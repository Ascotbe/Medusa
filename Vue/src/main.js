import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import Antd from 'ant-design-vue';
// import {
//     Button,
//     Layout,
//     Col,
//     Menu,
//     Dropdown,
//     Avatar,
//     Row,
//     Descriptions,
//     DatePicker,
//     Card,
//     Icon,
//     Upload,
//     Form,
//     Input,
//     Table,
//     Select,
//     Tag,
//     Tabs,
//     Divider,
//     Modal,
//     List,
//     Empty,
//     Progress,
//     Statistic,
//     Checkbox
// } from 'ant-design-vue';
// let components = [ 
//   Button,
//   Layout,
//   Col,
//   Menu,
//   Dropdown,
//   Avatar,
//   Row,
//   Descriptions,
//   DatePicker,
//   Card,
//   Icon,
//   Upload,
//   Form,
//   Input,
//   Table,
//   Select,
//   Tag,
//   Tabs,
//   Divider,
//   Modal,
//   List,
//   Empty,
//   Progress,
//   Statistic,
//   Checkbox
// ]
import axios from 'axios'
// import * as echarts from 'echarts';
// echarts改为按需引入，引入line,bar,pie三个
// 引入 echarts 核心模块，核心模块提供了 echarts 使用必须要的接口。
import * as echarts from 'echarts/core';
// 引入柱状图图表，图表后缀都为 Chart
import { LineChart,BarChart,PieChart,ScatterChart  } from 'echarts/charts';
// 引入提示框，标题，直角坐标系，数据集，内置数据转换器组件，组件后缀都为 Component
import {
  TitleComponent,
  TooltipComponent,
  GridComponent,
  DatasetComponent,
  TransformComponent,
  LegendComponent,
} from 'echarts/components';
// 标签自动布局，全局过渡动画等特性
import { LabelLayout, UniversalTransition } from 'echarts/features';
// 引入 Canvas 渲染器，注意引入 CanvasRenderer 或者 SVGRenderer 是必须的一步
import { CanvasRenderer } from 'echarts/renderers';

// 注册必须的组件
echarts.use([
  TitleComponent,
  TooltipComponent,
  GridComponent,
  DatasetComponent,
  TransformComponent,
  LegendComponent,
  LineChart,
  BarChart,
  PieChart,
  ScatterChart,
  LabelLayout,
  UniversalTransition,
  CanvasRenderer
]);

// import 'ant-design-vue/dist/antd.css';
import 'ant-design-vue/dist/antd.less'
import api from './api/rules'
Vue.use(Antd)
// components.forEach(e => {
//   Vue.use(e)
// })
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
