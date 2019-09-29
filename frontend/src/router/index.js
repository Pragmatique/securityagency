import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '@/components/Home'
import Lohin from '@/components/Login'
import CreateUser from '@/components/CreateUser'
import UserList from '@/components/UserList'

import Dashboard from '../pages/Dashboard.vue'
import Social from '../pages/Social.vue'
import Media from '../pages/Media.vue'
import Snackbar from '../pages/Snackbar.vue'
import Chart from '../pages/Chart.vue'
import Mailbox from '../pages/Mailbox.vue'
import Calendar from '../pages/Calendar.vue'
import Login from '../pages/core/Login.vue'
import Error from '../pages/core/Error.vue'

Vue.use(VueRouter)

export default new VueRouter({
  routes: [
    {
      path: '/first',
      name: 'Home',
      component: Home
    },
    {
      path: '/lohin',
      name: 'Lohin',
      component: Lohin
    },
    {
      path: '/signin',
      name: 'CreateUser',
      component: CreateUser
    },
    {
      path: '/userlist',
      name: 'UserList',
      component: UserList
    },
    {
      path: '/',
      name: 'Dashboard',
      component: Dashboard,
      meta: {
        breadcrumb: [
          { name: 'Dashboard' }
        ]
      }
    },
    {
      path: '/mailbox',
      name: 'Mailbox',
      component: Mailbox,
      meta: {
        breadcrumb: [
          { name: 'Dashboard', href: 'Dashboard' },
          { name: 'Mailbox' }
        ]
      }
    },
    {
      path: '/snackbar',
      name: 'Snackbar',
      component: Snackbar,
      meta: {
        breadcrumb: [
          { name: 'Dashboard', href: 'Dashboard' },
          { name: 'Snackbar' }
        ]
      }
    },
    {
      path: '/calendar',
      name: 'Calendar',
      component: Calendar,
      meta: {
        breadcrumb: [
          { name: 'Dashboard', href: 'Dashboard' },
          { name: 'Calendar' }
        ]
      }
    },
    {
      path: '/social',
      name: 'Social',
      component: Social,
      meta: {
        breadcrumb: [
          { name: 'Dashboard', href: 'Dashboard' },
          { name: 'Social' }
        ]
      }
    },
    {
      path: '/media',
      name: 'Media',
      component: Media,
      meta: {
        breadcrumb: [
          { name: 'Dashboard', href: 'Dashboard' },
          { name: 'Media' }
        ]
      }
    },
    {
      path: '/chart',
      name: 'Chart',
      component: Chart,
      meta: {
        breadcrumb: [
          { name: 'Dashboard', href: 'Dashboard' },
          { name: 'Chart' }
        ]
      }
    },
    {
      path: '/login',
      name: 'Login',
      component: Login,
      meta: {
        allowAnonymous: true
      }
    },
    {
      path: '/error',
      name: 'Error',
      component: Error,
      meta: {
        allowAnonymous: true
      }
    }
  ],
  mode: 'history'
})
