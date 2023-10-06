import { createRouter, createWebHistory } from 'vue-router';
import store from '@/store';

const routes = [
  {
    path: '/login',
    name: 'login',
    component: () => import('../views/LoginView.vue')
  },
  {
    path: '/admin',
    name: 'admin',
    component: () => import('../views/AdminView.vue'),
    children: [
      {
        path: 'basic',
        name: 'basic',
        component: () => import('../views/admin/BasicView.vue'),
        meta: {role: ['admin', 'user', 'manager'], title: "基本配置", is_menu: true},
      },
      {
        path: 'user',
        name: 'user',
        component: () => import('../views/admin/UserView.vue'),
        meta: {role: ['admin', 'manager'], title: "用户管理", is_menu: true},
      },
      {
        path: 'order',
        name: 'order',
        component: () => import('../views/admin/OrderView.vue'),
        meta: {role: ['admin', 'user'], title: "订单管理", is_menu: true},
      },
    ]
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.beforeEach((to, from, next) => {
  // console.log(to.meta.role);
  if (to.meta.role){
    let userRole = store.state.role;
    let allowRoleList = to.meta.role;
    if (allowRoleList.indexOf(userRole) === -1) {

      next({
        name: 'login'
      });
    } else{
      next();
    }
  } else{
    next();
  }
})

export default router
