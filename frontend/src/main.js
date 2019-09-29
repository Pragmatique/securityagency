// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import store from './store'
import VueResource from 'vue-resource'
import vuetify from './plugins/vuetify'

import 'vuetify/dist/vuetify.min.css';
// import 'font-awesome/css/font-awesome.css';

import Vuetify from 'vuetify';

// import 'material-design-icons-iconfont/dist/material-design-icons.css';
import './styles/global.css';

import axios from 'axios'
import VueAxios from 'vue-axios'

Vue.use(Vuetify);

Vue.config.productionTip = false

Vue.use(VueAxios, axios);

import VueChartkick from 'vue-chartkick';
import Chart from 'chart.js';
import fullCalendar from 'vue-fullcalendar';
import { setupComponents } from './config/setup-components';

import swatches from 'vue-swatches';
import "vue-swatches/dist/vue-swatches.min.css"

Vue.use(VueChartkick, { adapter: Chart });
Vue.component('full-calendar', fullCalendar);
Vue.component('swatches', swatches);

setupComponents(Vue);




/* Axios.interceptors.response.use((response) => {
  console.log('Step1')
  return response
}, (error) => {
  console.log('Step2')
  console.log(error.response.data)
  if (error.response.data.error.statusCode === 401) {
    store.dispatch('logout')
    router.push('/login')
  }
  return Promise.reject(error)
}
) */

/* eslint-disable no-new */
new Vue({
  el: '#app',
  store,
  router,
  components: { App },
  template: '<App/>',
  vuetify,
  data: {
    themeColor: '#1D2939',
    userEmail: 'admin@yopmail.com',
    userPassword: '123456'
  }
}).$mount('#app')
