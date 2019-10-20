import Vue from 'vue'
import App from './App.vue'
import router from './router'

import BootstrapVue from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import store from './store'

Vue.config.productionTip = process.env.NODE_ENV === 'production'
Vue.use(BootstrapVue)

new Vue({
  render: h => h(App),
  router,
  store,
}).$mount('#app')
