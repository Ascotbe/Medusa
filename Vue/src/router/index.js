import Vue from 'vue'
import VueRouter from 'vue-router'
import login from '../LoginAndForget/login/index.vue'
import register from '../LoginAndForget/register/register.vue'

import layout from '../layout'
// import personalSettings from '../layout/personalSettings'
import personalSettings2 from '../layout/personalSettings/index2'
import setpassword from '../layout/personalSettings/setpassword/setpassword.vue'
import dashboard from '../layout/dashboard'
import siteScan from '../layout/siteInformation/siteScan/siteScan.vue'
import siteInformation from '../layout/siteInformation/siteInformation.vue'
import vulnerabilityDetails2 from '../layout/siteInformation/siteScan/vulnerabilityDetails/vulnerabilityDetails2.vue'
import vulnerabilityDetails from '../layout/siteInformation/siteScan/vulnerabilityDetails/vulnerabilityDetails.vue'
import gitHub from '../layout/gitHub/gitHub.vue'
import Agreement from '../LoginAndForget/agreement/agreement.vue'
import Forget from '../LoginAndForget/forget/forget.vue'
import issueTasks from '../layout/issueTasks/issueTasks.vue'
import createProject from '../layout/scriptFish/createProject/createProject.vue'


import projectManagement from '../layout/scriptFish/projectManagement/projectManagement.vue'
import selectProject from '../layout/scriptFish/projectManagement/selectProject/selectProject.vue'
import projectDetails from '../layout/scriptFish/projectManagement/projectDetails/projectDetails.vue'
import publicTemplate from '../layout/scriptFish/publicTemplate/publicTemplate.vue'
import customTemplate from '../layout/scriptFish/customTemplate/customTemplate.vue'

import combinedList from '../layout/combine/combineList/combineList.vue'
import markdownData from '../layout/combine/combineList/markdownData/markdownData.vue'
import dataComparison from '../layout/combine/combineList/markdownData/dataComparison.vue'
import createCombine from '../layout/combine/createCombine/createCombine.vue'

import antivirusSoftwareCompared from '../layout/toolbar/antivirusSoftwareCompared/antivirusSoftwareCompared.vue'

import AboutUs from '../layout/AboutUs/AboutUs.vue'
import DomainNameSystemLog from '../layout/DomainNameSystemLog/DNSLog.vue'

import CommonVulnerabilitiesAndExposures from '../layout/CommonVulnerabilitiesAndExposuresMonitor/CommonVulnerabilitiesAndExposures.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Login',
    // component: Login
    component: login
    // component:()=> import('@views/login/index')
  },

  {
    path: '/Agreement',
    name: 'Agreement',
    // component: Login
    component: Agreement
    // component:()=> import('@views/login/index')
  },
  {
    path: '/Register',
    name: 'Register',
    // component: Login
    component: register
    // component:()=> import('@views/login/index')
  },
  {
    path: '/Forget',
    name: 'Forget',
    // component: Login
    component: Forget
  },
  {
    path: '/setpassword',
    name: 'setpassword',
    // component: Login
    component: setpassword
  },
  {
    path: '/layout',
    name: 'layout',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: layout,
    redirect: '/layout/dashboard',
    children: [
      {
        path: 'personalSettings',
        component: personalSettings2,
        name: 'personalSettings',
        meta: {
          keepAlive: true,
          activeIndex: "personalSettings"
        },
      },
      {
        path: 'dashboard',
        component: dashboard,
        name: 'dashboard',
        meta: {
          keepAlive: true,
          activeIndex: "dashboard"
        },
      },
      {
        path: 'siteInformation',
        component: siteInformation,
        name: 'siteInformation',
        meta: {
          keepAlive: true,
          activeIndex: "siteInformation",
          defaultOpenKeys: "sub1"
        },
      },
      {
        path: 'siteInformation/siteScan',
        component: siteScan,
        name: 'siteInformation/siteScan',
        meta: {
          keepAlive: true,
          activeIndex: "siteInformation",
          defaultOpenKeys: "sub1"
        },
      },
      {
        path: 'siteInformation/siteScan/vulnerabilityDetails',
        component: vulnerabilityDetails,
        name: 'siteInformation/siteScan/vulnerabilityDetails',
        meta: {
          keepAlive: true,
          activeIndex: "siteInformation",
          defaultOpenKeys: "sub1"
        },
      },
      {
        path: 'siteInformation/siteScan/vulnerabilityDetails2',
        component: vulnerabilityDetails2,
        name: 'siteInformation/siteScan/vulnerabilityDetails2',
        meta: {
          keepAlive: true,
          activeIndex: "siteInformation",
          defaultOpenKeys: "sub1"
        },
      },
      // {
      //   path: 'siteInformation/siteScan/domainNameDetails',
      //   component: domainNameDetails,
      //   name: 'siteInformation/siteScan/domainNameDetails'
      // },
      {
        path: 'issueTasks',
        component: issueTasks,
        name: 'issueTasks',
        meta: {
          keepAlive: true,
          activeIndex: "issueTasks",
          defaultOpenKeys: "sub1"
        },

      },
      {
        path: 'gitHub',
        component: gitHub,
        name: 'gitHub',
        meta: {
          keepAlive: true,
          activeIndex: "gitHub",
          defaultOpenKeys: "sub3"
        },
      },
      {
        path: 'createProject',
        component: createProject,
        name: 'createProject',
        meta: {
          keepAlive: true,
          activeIndex: "createProject",
          defaultOpenKeys: "sub4"
        },
      },

      {
        path: 'projectManagement',
        component: projectManagement,
        name: 'projectManagement',
        meta: {
          keepAlive: true,
          activeIndex: "projectManagement",
          defaultOpenKeys: "sub4"
        },
      },
      {
        path: 'projectManagement/selectProject',
        component: selectProject,
        name: 'projectManagement/selectProject',
        meta: {
          keepAlive: true,
          activeIndex: "projectManagement",
          defaultOpenKeys: "sub4"
        },
      },
      {
        path: 'projectManagement/projectDetails',
        component: projectDetails,
        name: 'projectManagement/projectDetails',
        meta: {
          keepAlive: true,
          activeIndex: "projectManagement",
          defaultOpenKeys: "sub4"
        },
      },
      {
        path: 'publicTemplate',
        component: publicTemplate,
        name: 'publicTemplate',
        meta: {
          keepAlive: true,
          activeIndex: "publicTemplate",
          defaultOpenKeys: "sub4"
        },
      },
      {
        path: 'customTemplate',
        component: customTemplate,
        name: 'customTemplate',
        meta: {
          keepAlive: true,
          activeIndex: "customTemplate",
          defaultOpenKeys: "sub4"
        },
      },
      {
        path: 'combinedList',
        component: combinedList,
        name: 'combinedList',
        meta: {
          keepAlive: true,
          activeIndex: "combinedList",
          defaultOpenKeys: "sub5"
        },
      },
      {
        path: 'combinedList/markdownData',
        component: markdownData,
        name: 'combinedList/markdownData',
        meta: {
          keepAlive: true,
          activeIndex: "combinedList",
          defaultOpenKeys: "sub5"
        },
      },
      {
        path: 'combinedList/markdownData/dataComparison',
        component: dataComparison,
        name: 'combinedList/markdownData/dataComparison',
        meta: {
          keepAlive: true,
          activeIndex: "combinedList",
          defaultOpenKeys: "sub5"
        },
      },
      {
        path: 'createCombine',
        component: createCombine,
        name: 'createCombine',
        meta: {
          keepAlive: true,
          activeIndex: "createCombine",
          defaultOpenKeys: "sub5"
        },
      },
      {
        path: 'antivirusSoftwareCompared',
        component: antivirusSoftwareCompared,
        name: 'antivirusSoftwareCompared',
        meta: {
          keepAlive: true,
          activeIndex: "antivirusSoftwareCompared",
          defaultOpenKeys: "sub6"
        },

      },
      {
        path: 'about_us',
        component: AboutUs,
        name: 'about_us',
        meta: {
          keepAlive: true,
          activeIndex: "about_us",
        },

      },
      {
        path: 'domain_name_system_log',
        component: DomainNameSystemLog,
        name: 'domain_name_system_log',
        meta: {
          keepAlive: true,
          activeIndex: "domain_name_system_log",
        },

      },
      {
        path: 'nist_data_bulk_query',
        component: CommonVulnerabilitiesAndExposures,
        name: 'nist_data_bulk_query',
        meta: {
          keepAlive: true,
          activeIndex: "nist_data",
          defaultOpenKeys: "sub3"
        },
      },

    ]
  },
]
const originalPush = VueRouter.prototype.push
VueRouter.prototype.push = function push(location) {
  return originalPush.call(this, location).catch(err => err)
}
const router = new VueRouter({
  routes,
  // scrollBehavior(to,from,savePosition){
  //   if(savePosition){
  //     return savePosition
  //   }
  //   else{
  //     return{
  //       x:0,
  //       y:0
  //     }
  //   }
  // }
})

export default router
