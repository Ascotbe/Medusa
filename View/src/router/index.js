import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

/* Layout */
import Layout from '@/layout'

/* Router Modules */
import componentsRouter from './modules/components'
import chartsRouter from './modules/charts'
import tableRouter from './modules/table'
import nestedRouter from './modules/nested'

/**
 * Note: sub-menu only appear when route children.length >= 1
 * Detail see: https://panjiachen.github.io/vue-element-admin-site/guide/essentials/router-and-nav.html
 *
 * hidden: true                   if set true, item will not show in the sidebar(default is false)
 * alwaysShow: true               if set true, will always show the root menu
 *                                if not set alwaysShow, when item has more than one children route,
 *                                it will becomes nested mode, otherwise not show the root menu
 * redirect: noRedirect           if set noRedirect will no redirect in the breadcrumb
 * name:'router-name'             the name is used by <keep-alive> (must set!!!)
 * meta : {
    roles: ['admin','editor']    control the page roles (you can set multiple roles)
    title: 'title'               the name show in sidebar and breadcrumb (recommend set)
    icon: 'svg-name'             the icon show in the sidebar
    noCache: true                if set true, the page will no be cached(default is false)
    affix: true                  if set true, the tag will affix in the tags-view
    breadcrumb: false            if set false, the item will hidden in breadcrumb(default is true)
    activeMenu: '/example/list'  if set path, the sidebar will highlight the path you set
  }
 */

/**
 * 实例化Vue时只挂载ConstantRoutes
 * constantRoutes
 * a base page that does not have permission requirements
 * all roles can be accessed
 */

// 所有权限通用路由表，例如首页和登陆页以及一些不用权限的公用页面

export const constantRoutes = [
  {
    path: '/redirect',
    component: Layout,
    hidden: true,
    children: [
      {
        path: '/redirect/:path(.*)',
        component: () => import('@/views/redirect/index')
      }
    ]
  },
  {
    path: '/login',
    component: () => import('@/views/login/index'),
    hidden: true
  },
  {
    path: '/auth-redirect',
    component: () => import('@/views/login/auth-redirect'),
    hidden: true
  },
  {
    path: '/404',
    component: () => import('@/views/error-page/404'),
    hidden: true
  },
  {
    path: '/401',
    component: () => import('@/views/error-page/401'),
    hidden: true
  },
  {
    path: '/',
    component: Layout,
    redirect: '/dashboard',
    children: [
      {
        path: 'dashboard',
        component: () => import('@/views/dashboard/index'),
        name: 'Dashboard',
        meta: { title: '仪表盘', icon: 'dashboard', affix: true }
      }
    ]
  },


  {
    path: '/guide',
    component: Layout,
    redirect: '/guide/index',
    children: [
      {
        path: 'index',
        component: () => import('@/views/guide/index'),
        name: 'Guide',
        meta: { title: '导航', icon: 'guide', noCache: true }
      }
    ]
  },
  {
    path: '/profile',
    component: Layout,
    redirect: '/profile/index',
    hidden: true,
    children: [
      {
        path: 'index',
        component: () => import('@/views/profile/index'),
        name: 'Profile',
        meta: { title: '设置', icon: 'user', noCache: true }
      }
    ]
  }
]

/**
 * 异步挂载的路由，动态需要根据权限
 * asyncRoutes
 * the routes that need to be dynamically loaded based on user roles
 */
export const asyncRoutes = [
  // {
  //   path: '/permission',
  //   component: Layout,
  //   redirect: '/permission/page',
  //   alwaysShow: true, // will always show the root menu
  //   name: 'Permission',
  //   meta: {
  //     title: '权限测试页',
  //     icon: 'lock',
  //     roles: ['admin', 'editor'] // you can set roles in root nav
  //   },
  //   children: [
  //     {
  //       path: 'page',
  //       component: () => import('@/views/permission/page'),
  //       name: 'PagePermission',
  //       meta: {
  //         title: 'Page Permission',
  //         roles: ['admin'] // or you can only set roles in sub nav
  //       }
  //     },
  //     {
  //       path: 'directive',
  //       component: () => import('@/views/permission/directive'),
  //       name: 'DirectivePermission',
  //       meta: {
  //         title: 'Directive Permission'
  //         // if do not set roles, means: this page does not require permission
  //       }
  //     },
  //     {
  //       path: 'role',
  //       component: () => import('@/views/permission/role'),
  //       name: 'RolePermission',
  //       meta: {
  //         title: 'Role Permission',
  //         roles: ['admin']
  //       }
  //     }
  //   ]
  // },

  // {
  //   path: '/icon',
  //   component: Layout,
  //   children: [
  //     {
  //       path: 'index',
  //       component: () => import('@/views/icons/index'),
  //       name: 'Icons',
  //       meta: { title: '标签', icon: 'icon', noCache: true }
  //     }
  //   ]
  // },

  /** when your routing map is too long, you can split it into small modules **/
  // componentsRouter,
  // chartsRouter,
  // nestedRouter,
  // tableRouter,


  {
    path: '/error-log',
    component: Layout,
    children: [
      {
        path: 'log',
        component: () => import('@/views/error-log/index'),
        name: 'Error Log',
        meta: { title: '错误日志', icon: 'bug' }
      }
    ]
  },

  {
      path: '/active_scan',
      component: Layout,
      redirect: '/active_scan/site_scan',
      name: 'active_scan',
      meta: {
        title: '主动扫描',
        icon: 'scan'
      },
      children: [
        {
          path: 'bugs_information',
          component: () => import('@/views/active_scan/bugs_information'),
          name: 'bugs-information',
          meta: { title: '漏洞信息' }
        },
        {
          path: 'site_scan',
          component: () => import('@/views/active_scan/site_scan'),
          name: 'site_scan',
          meta: { title: '站点扫描' }
        },
        {
          path: 'service_information',
          component: () => import('@/views/active_scan/service_information'),
          name: 'service_information',
          meta: { title: '服务信息' }
        }
      ]
   },

   {
      path: '/passive_scan',
      component: Layout,
      redirect: '/passive_scan/add_item',
      name: 'passive_scan',
      meta: {
        title: '被动扫描',
        icon: 'scan'
      },
      children: [
        {
          path: 'bug_informations',
          component: () => import('@/views/passive_scan/bug_informations'),
          name: 'bug_informations',
          meta: { title: '漏洞信息' }
        },
        {
          path: 'add_item',
          component: () => import('@/views/passive_scan/add_item'),
          name: 'add_item',
          meta: { title: '添加目标' }
        },
        {
          path: 'scan_record',
          component: () => import('@/views/passive_scan/scan_record'),
          name: 'scan_record',
          meta: { title: '扫描记录' }
        },
        {
          path: 'item_manager',
          component: () => import('@/views/passive_scan/item_manager'),
          name: 'item_manager',
          meta: { title: '项目管理' }
        }
      ]
   },

   {
     path: '/test',
     component: Layout,
     redirect: '/test/index',
     name: 'index',
     meta: {
       title: 'index',
       icon: 'moon'
     },
     children: [
       {
         path: 'index',
         component: ()=>import('@/views/test/index'),
         name: 'test',
         meta: { title: '测试页面' }
       }
     ]
   },

   {
      path: '/addin',
      component: Layout,
      redirect: '/addin/add_plug-in',
      name: 'addin',
      meta: {
        title: '生态插件',
        icon: 'plug'
      },
      children: [
        {
          path: 'add_plug-in',
          component: () => import('@/views/addin/add_plug-in'),
          name: 'add_plug',
          meta: { title: '添加插件' }
        },
        {
          path: 'plug_list',
          component: () => import('@/views/addin/plug_list'),
          name: 'plug_list',
          meta: { title: '插件列表' }
        },
        {
          path: 'my_plug_in',
          component: () => import('@/views/addin/my_plug_in'),
          name: 'my_plug_in',
          meta: { title: '我的插件' }
        }
      ]
   },

  // 404 page must be placed at the end !!!
  { path: '*', redirect: '/404', hidden: true }
]

const createRouter = () => new Router({
  // mode: 'history', // require service support
  scrollBehavior: () => ({ y: 0 }),
  routes: constantRoutes
})

const router = createRouter()

// Detail see: https://github.com/vuejs/vue-router/issues/1234#issuecomment-357941465
export function resetRouter() {
  const newRouter = createRouter()
  router.matcher = newRouter.matcher // reset router
}

export default router
