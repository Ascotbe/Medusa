import Vue from 'vue'
import VueRouter from 'vue-router'
import Dashboard from '../views/Dashboard/Dashboard.vue'
import Login from '../views/Login/Login.vue'
import Register from '../views/Register/Register.vue'
import Layout from '../views/Layout/Layout.vue'
import PersonalSettings from '../views/PersonalSettings/PersonalSettings.vue'
import IssueTask from '../views/ActiveScanning/IssueTask/IssueTask.vue'
import SiteInforMation from '../views/ActiveScanning/SiteInforMation/SiteInforMation.vue'
import GitHubMonitor from '../views/Monitor/GitHubMonitor/GitHubMonitor.vue'
import VulnerabilitiesMonitor from '../views/Monitor/VulnerabilitiesMonitor/VulnerabilitiesMonitor.vue'
import VulnerabilitiesMonitorDetailed from '../views/Monitor/VulnerabilitiesMonitor/part/VulnerabilitiesMonitorDetailed.vue'
import CreateCombine from '../views/Combine/CreateCombine/CreateCombine.vue'
import CombineList from '../views/Combine/CombineList/CombineList.vue'



import { message } from 'ant-design-vue'
import store from '@/store'

// import { mapGetters } from "vuex";

Vue.use(VueRouter)

const routes = [
  {
    path: '/login',
    name: 'login',
    component: Login
  },
  {
    path: '/register',
    name: 'register',
    component: Register
  },
  {
    path: '/',
    name: 'layout',
    component: Layout,
    redirect: '/layout/dashboard',
  },
  {
    path: '/layout',
    name: 'layout',
    component: Layout,
    meta: {
      isLogin: true
    },
    redirect: '/layout/dashboard',
    children: [{
      path: 'dashboard',
      name: 'dashboard',
      component: Dashboard,
    },
    {
      path: 'personalSettings',
      name: 'personalSettings',
      component: PersonalSettings,
    },
    {
      path: 'issueTasks',
      name: 'issueTasks',
      component: IssueTask,
    },
    {
      path: 'siteInformation',
      name: 'siteInformation',
      component: SiteInforMation,
    },
    {
      path: 'GitHubMonitor',
      name: 'GitHubMonitor',
      component: GitHubMonitor,
    },
    {
      path: 'VulnerabilitiesMonitor',
      name: 'VulnerabilitiesMonitor',
      component: VulnerabilitiesMonitor,
    },
    {
      path: 'VulnerabilitiesMonitorDetailed',
      name: 'VulnerabilitiesMonitor/VulnerabilitiesMonitorDetailed',
      component: VulnerabilitiesMonitorDetailed,
    },
    {
      path: 'CreateCombine',
      name: 'CreateCombine',
      component: CreateCombine,
    },
    {
      path: 'CombineList',
      name: 'CombineList',
      component: CombineList,
    },

    ]
  },
]

const originalPush = VueRouter.prototype.push
VueRouter.prototype.push = function push (location) {
  return originalPush.call(this, location).catch(err => err)
}

const router = new VueRouter({
  routes
})

router.beforeEach(async (to, from, next) => {
  if (to.name == from.name) {
    next(false)
    return
  }
  if (to.matched[0]?.meta.isLogin) {
    if (localStorage.getItem('token')) {
      await store.dispatch("UserStore/setUserinfo", localStorage.getItem('token'))
      if (store.state.UserStore.userinfo.key) {
        if (to.name.indexOf('/') != -1) store.commit("StateStore/setStarSelectedKeys", to.name.substring(0, to.name.indexOf('/')))
        else store.commit("StateStore/setStarSelectedKeys", to.name)
        next()
      }
      else {
        message.warn('用户信息获取失败')
        next({
          path: "/login",
        });
      }
    } else {
      message.warn('未登录')
      next({
        path: "/login",
      });
    }
  } else {
    next()
  }
})

export default router