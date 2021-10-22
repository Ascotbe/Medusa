import Vue from 'vue'
import VueRouter from 'vue-router'
import Login from '../views/Login/Login.vue'
import Register from '../views/Register/Register.vue'
import ForgetPassWord from '../views/ForgetPassWord/ForgetPassWord.vue'
import RevisePassWord from '../views/RevisePassWord/RevisePassWord.vue'
import Layout from '../views/Layout/Layout.vue'
//仪表盘首页
import Dashboard from '../views/Dashboard/Dashboard.vue'
//个人信息
import PersonalSettings from '../views/PersonalSettings/PersonalSettings.vue'
//主动扫描
import IssueTask from '../views/ActiveScanning/IssueTask/IssueTask.vue'
import SiteInforMation from '../views/ActiveScanning/SiteInforMation/SiteInforMation.vue'
//监控
import GitHubMonitor from '../views/Monitor/GitHubMonitor/GitHubMonitor.vue'
import VulnerabilitiesMonitor from '../views/Monitor/VulnerabilitiesMonitor/VulnerabilitiesMonitor.vue'
import VulnerabilitiesMonitorDetailed from '../views/Monitor/VulnerabilitiesMonitor/part/VulnerabilitiesMonitorDetailed.vue'
//协同
import CreateCombine from '../views/Combine/CreateCombine/CreateCombine.vue'
import CombineList from '../views/Combine/CombineList/CombineList.vue'
import MarkdownData from '../views/Combine/CombineList/part/MarkdownData.vue'
import DataComparison from '../views/Combine/CombineList/part/DataComparison.vue'
//XSS
import CreateCrossSiteScript from '../views/CrossSiteScript/CreateCrossSiteScript/CreateCrossSiteScript.vue'
import ProjectManagement from '../views/CrossSiteScript/ProjectManagement/ProjectManagement.vue'
import QueryProject from '../views/CrossSiteScript/ProjectManagement/part/QueryProject.vue'
import ModifyProject from '../views/CrossSiteScript/ProjectManagement/part/ModifyProject.vue'
import TemplateManagement from '../views/CrossSiteScript/TemplateManagement/TemplateManagement.vue'
import PrivateTemplate from '../views/CrossSiteScript/PrivateTemplate/PrivateTemplate.vue'
//工具库
import DNSLOG from '../views/DNSLOG/DNSLOG.vue'
//ShellCode
import ShellCodeToTrojan from '../views/ShellCode/ShellCodeToTrojan/ShellCodeToTrojan.vue'
//关于
import About from '../views/About/About.vue'



import { message } from 'ant-design-vue'
import store from '@/store'

// import { mapGetters } from "vuex";

Vue.use(VueRouter)

const routes = [
  //重定向
  {
    path: '/',
    name: 'layout',
    component: Layout,
    redirect: '/layout/dashboard',
  },
  //登录
  {
    path: '/login',
    name: 'login',
    component: Login
  },
  //注册
  {
    path: '/register',
    name: 'register',
    component: Register
  },
  //忘记密码
  {
    path: '/ForgetPassWord',
    name: 'ForgetPassWord',
    component: ForgetPassWord
  },
  //修改密码
  {
    path: '/RevisePassWord',
    name: 'RevisePassWord',
    component: RevisePassWord,
    meta: {
      isLogin: true
    },
  },
  //布局页
  {
    path: '/layout',
    name: 'layout',
    component: Layout,
    meta: {
      isLogin: true
    },
    redirect: '/layout/dashboard',
    children: [
      //仪表盘
      {
        path: 'dashboard',
        name: 'dashboard',
        component: Dashboard,
      },
      //个人界面
      {
        path: 'personalSettings',
        name: 'personalSettings',
        component: PersonalSettings,
      },
      //主动攻击
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
      //监控页面
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
      //协同作战
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
      {
        path: 'MarkdownData',
        name: 'CombineList/MarkdownData',
        component: MarkdownData,
      },
      {
        path: 'DataComparison',
        name: 'CombineList/DataComparison',
        component: DataComparison,
      },
      //跨站脚本钓鱼
      {
        path: 'CreateCrossSiteScript',
        name: 'CreateCrossSiteScript',
        component: CreateCrossSiteScript,
      },
      {
        path: 'ProjectManagement',
        name: 'ProjectManagement',
        component: ProjectManagement,
      },
      {
        path: 'QueryProject',
        name: 'ProjectManagement/QueryProject',
        component: QueryProject,
      },
      {
        path: 'ModifyProject',
        name: 'ProjectManagement/ModifyProject',
        component: ModifyProject,
      },
      {
        path: 'TemplateManagement',
        name: 'TemplateManagement',
        component: TemplateManagement,
      },
      {
        path: 'PrivateTemplate',
        name: 'PrivateTemplate',
        component: PrivateTemplate,
      },
      //DNSLOG
      {
        path: 'DNSLOG',
        name: 'DNSLOG',
        component: DNSLOG,
      },
      //ShellCode
      {
        path: 'ShellCodeToTrojan',
        name: 'ShellCodeToTrojan',
        component: ShellCodeToTrojan,
      },
      //About
      {
        path: 'About',
        name: 'About',
        component: About,
      },
    ]
  },
  // 最后是404页面
  // {
  //   path: '*',
  //   meta: { requireAuth: true },
  //   component: Notfound
  // }
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