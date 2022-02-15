import Vue from 'vue'
import VueRouter from 'vue-router'
// import Login from '../views/Login/Login.vue'
// import Register from '../views/Register/Register.vue'
// import ForgetPassWord from '../views/ForgetPassWord/ForgetPassWord.vue'
// import RevisePassWord from '../views/RevisePassWord/RevisePassWord.vue'
// import Layout from '../views/Layout/Layout.vue'
//仪表盘首页
// import Dashboard from '../views/Dashboard/Dashboard.vue'
//个人信息
// import PersonalSettings from '../views/PersonalSettings/PersonalSettings.vue'
//主动扫描
// import IssueTask from '../views/ActiveScanning/IssueTask/IssueTask.vue'
// import SiteInforMation from '../views/ActiveScanning/SiteInforMation/SiteInforMation.vue'
//监控
// import GitHubMonitor from '../views/Monitor/GitHubMonitor/GitHubMonitor.vue'
// import VulnerabilitiesMonitor from '../views/Monitor/VulnerabilitiesMonitor/VulnerabilitiesMonitor.vue'
// import VulnerabilitiesMonitorDetailed from '../views/Monitor/VulnerabilitiesMonitor/part/VulnerabilitiesMonitorDetailed.vue'
//协同
// import CreateCombine from '../views/Combine/CreateCombine/CreateCombine.vue'
// import CombineList from '../views/Combine/CombineList/CombineList.vue'
// import MarkdownData from '../views/Combine/CombineList/part/MarkdownData.vue'
// import DataComparison from '../views/Combine/CombineList/part/DataComparison.vue'
//XSS
// import CreateCrossSiteScript from '../views/CrossSiteScript/CreateCrossSiteScript/CreateCrossSiteScript.vue'
// import ProjectManagement from '../views/CrossSiteScript/ProjectManagement/ProjectManagement.vue'
// import QueryProject from '../views/CrossSiteScript/ProjectManagement/part/QueryProject.vue'
// import ModifyProject from '../views/CrossSiteScript/ProjectManagement/part/ModifyProject.vue'
// import TemplateManagement from '../views/CrossSiteScript/TemplateManagement/TemplateManagement.vue'
// import PrivateTemplate from '../views/CrossSiteScript/PrivateTemplate/PrivateTemplate.vue'
//DNSLOG
// import DNS from '../views/DNSLOG/DNS/DNS.vue'
// import HTTP from '../views/DNSLOG/HTTP/HTTP.vue'


//ShellCode
// import ShellCodeToTrojan from '../views/ShellCode/ShellCodeToTrojan/ShellCodeToTrojan.vue'
//关于
// import About from '../views/About/About.vue'
//邮件
// import SendMail from '../views/Mail/SendMail/SendMail.vue'


import { message } from 'ant-design-vue'
import store from '@/store'

// import { mapGetters } from "vuex";

Vue.use(VueRouter)

const routes = [
  //重定向
  {
    path: '/',
    name: 'layout',
    // component: Layout,
    // component: () => import('@/views/Layout/Layout'),
    redirect: '/layout/dashboard',
  },
  //登录
  {
    path: '/login',
    name: 'login',
    // component: Login
    component: () => import('@/views/Login/Login'),
  },
  //注册
  {
    path: '/register',
    name: 'register',
    // component: Register
    component: () => import('@/views/Register/Register')
  },
  //忘记密码
  {
    path: '/ForgetPassWord',
    name: 'ForgetPassWord',
    // component: ForgetPassWord
    component:  () => import('@/views/ForgetPassWord/ForgetPassWord')
  },
  //修改密码
  {
    path: '/RevisePassWord',
    name: 'RevisePassWord',
    // component: RevisePassWord,
    component:  () => import('@/views/RevisePassWord/RevisePassWord'),
    meta: {
      isLogin: true
    },
  },
  //布局页
  {
    path: '/layout',
    name: 'layout',
    // component: Layout,
    component: () => import('@/views/Layout/Layout'),
    meta: {
      isLogin: true
    },
    redirect: '/layout/dashboard',
    children: [
      //仪表盘
      {
        path: 'dashboard',
        name: 'dashboard',
        // component: Dashboard,
        component: () => import('@/views/Dashboard/Dashboard'),
      },
      //个人界面
      {
        path: 'personalSettings',
        name: 'personalSettings',
        // component: PersonalSettings,
        component: () => import('@/views/PersonalSettings/PersonalSettings'),
      },
      //主动攻击
      {
        path: 'issueTasks',
        name: 'issueTasks',
        // component: IssueTask,
        component: () => import('@/views/ActiveScanning/IssueTask/IssueTask'),
      },
      {
        path: 'siteInformation',
        name: 'siteInformation',
        // component: SiteInforMation,
        component: () => import('@/views/ActiveScanning/SiteInforMation/SiteInforMation'),
      },
      //监控页面
      {
        path: 'GitHubMonitor',
        name: 'GitHubMonitor',
        // component: GitHubMonitor,
        component: () => import('@/views/Monitor/GitHubMonitor/GitHubMonitor'),
      },
      {
        path: 'VulnerabilitiesMonitor',
        name: 'VulnerabilitiesMonitor',
        // component: VulnerabilitiesMonitor,
        component: () => import('@/views/Monitor/VulnerabilitiesMonitor/VulnerabilitiesMonitor'),
      },
      {
        path: 'VulnerabilitiesMonitorDetailed',
        name: 'VulnerabilitiesMonitor/VulnerabilitiesMonitorDetailed',
        // component: VulnerabilitiesMonitorDetailed,
        component: () => import('@/views/Monitor/VulnerabilitiesMonitor/part/VulnerabilitiesMonitorDetailed'),
      },
      //协同作战
      {
        path: 'CreateCombine',
        name: 'CreateCombine',
        // component: CreateCombine,
        component: () => import('@/views/Combine/CreateCombine/CreateCombine'),
      },
      {
        path: 'CombineList',
        name: 'CombineList',
        // component: CombineList,
        component: () => import('@/views/Combine/CombineList/CombineList'),
      },
      {
        path: 'MarkdownData',
        name: 'CombineList/MarkdownData',
        // component: MarkdownData,
        component: () => import('@/views/Combine/CombineList/part/MarkdownData'),
      },
      {
        path: 'DataComparison',
        name: 'CombineList/DataComparison',
        // component: DataComparison,
        component: () => import('@/views/Combine/CombineList/part/DataComparison'),
      },
      //跨站脚本钓鱼
      {
        path: 'CreateCrossSiteScript',
        name: 'CreateCrossSiteScript',
        // component: CreateCrossSiteScript,
        component: () => import('@/views/CrossSiteScript/CreateCrossSiteScript/CreateCrossSiteScript'),
      },
      {
        path: 'ProjectManagement',
        name: 'ProjectManagement',
        // component: ProjectManagement,
        component: () => import('@/views/CrossSiteScript/ProjectManagement/ProjectManagement'),
      },
      {
        path: 'QueryProject',
        name: 'ProjectManagement/QueryProject',
        // component: QueryProject,
        component: () => import('@/views/CrossSiteScript/ProjectManagement/part/QueryProject'),
      },
      {
        path: 'ModifyProject',
        name: 'ProjectManagement/ModifyProject',
        // component: ModifyProject,
        component: () => import('@/views/CrossSiteScript/ProjectManagement/part/ModifyProject'),
      },
      {
        path: 'TemplateManagement',
        name: 'TemplateManagement',
        // component: TemplateManagement,
        component: () => import('@/views/CrossSiteScript/TemplateManagement/TemplateManagement'),
      },
      {
        path: 'PrivateTemplate',
        name: 'PrivateTemplate',
        // component: PrivateTemplate,
        component: () => import('@/views/CrossSiteScript/PrivateTemplate/PrivateTemplate'),
      },
      // 工具栏
      {
        path: 'antivirusSoftwareCompared',
        name: 'antivirusSoftwareCompared',
      },
      //DNSLOG
      {
        path: 'DNS',
        name: 'DNS',
        // component: DNS,
        component: () => import('@/views/DNSLOG/DNS/DNS'),
      },
      {
        path: 'HTTP',
        name: 'HTTP',
        // component: HTTP,
        component: () => import('@/views/DNSLOG/HTTP/HTTP'),
      },
      //ShellCode
      {
        path: 'ShellCodeToTrojan',
        name: 'ShellCodeToTrojan',
        // component: ShellCodeToTrojan,
        component: () => import('@/views/ShellCode/ShellCodeToTrojan/ShellCodeToTrojan'),
      },
      //About
      {
        path: 'About',
        name: 'About',
        // component: About,
        component: () => import('@/views/About/About'),
      },
      //邮件发送
      {
        path: 'SendMail',
        name: 'SendMail',
        // component: SendMail,
        component: () => import('@/views/Mail/SendMail/SendMail'),
      },
      //邮件列表
      {
        path: 'MailList',
        name: 'MailList',
        // component: SendMail,
        component: () => import('@/views/Mail/MailList'),
      },
      // 邮件详情
      {
        path: 'MailDetail',
        name: 'MailDetail',
        // component: SendMail,
        component: () => import('@/views/Mail/MailDetail'),
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