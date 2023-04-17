import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/SignIn',
    name: 'SignIn',
    component: () => import('../views/SignIn')
  },
  {
    path: '/SignUp',
    name: 'SignUp',
    component: () => import('../views/SignUp')
  },
  {
    path: '/user',
    name: 'User',
    component: () => import('../views/User')
  },
  {
    path: '/test',
    name: 'test',
    component: () => import('../views/Test')
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
