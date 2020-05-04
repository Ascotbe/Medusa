/** When your routing table is too long, you can split it into small modules **/

import Layout from '@/layout'

const nestedRouter = {
  path: '/nested',
  component: Layout,
  redirect: '/nested/menu1/menu1-1',
  name: 'Nested',
  meta: {
    title: '资产管理',
    icon: 'nested'
  },
  children: [
    {
      path: 'menu1',
      component: () => import('@/views/nested/menu1/index'), // Parent router-view
      name: 'Menu1',
      meta: { title: '资产列表' },
      redirect: '/nested/menu1/menu1-1',
      children: [
        {
          path: 'menu1-1',
          component: () => import('@/views/nested/menu1/menu1-1'),
          name: 'Menu1-1',
          meta: { title: '资产列表' }
        }
        // {
        //   path: 'menu1-2',
        //   component: () => import('@/views/nested/menu1/menu1-2'),
        //   name: 'Menu1-2',
        //   redirect: '/nested/menu1/menu1-2/menu1-2-1',
        //   meta: { title: '子资产列表' },
        //   children: [
        //     {
        //       path: 'menu1-2-1',
        //       component: () => import('@/views/nested/menu1/menu1-2/menu1-2-1'),
        //       name: 'Menu1-2-1',
        //       meta: { title: 'Menu 1-2-1' }
        //     },
        //     {
        //       path: 'menu1-2-2',
        //       component: () => import('@/views/nested/menu1/menu1-2/menu1-2-2'),
        //       name: 'Menu1-2-2',
        //       meta: { title: '还不知道写啥' }
        //     }
        //   ]
        // }
        // {
        //   path: 'menu1-3',
        //   component: () => import('@/views/nested/menu1/menu1-3'),
        //   name: 'Menu1-3',
        //   meta: { title: 'Menu 1-3' }
        // }
      ]
    },
    {
      path: 'menu2',
      name: 'Menu2',
      component: () => import('@/views/nested/menu2/index'),
      meta: { title: '端口服务' }
    },
    {
      path: 'menu3',
      name: 'Menu3',
      component: () => import('@/views/nested/menu3/index'),
      meta: { title: '子资产列表' }
    }
  ]
}

export default nestedRouter
