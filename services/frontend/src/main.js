import 'bootstrap/dist/css/bootstrap.css'
import axios from 'axios'
import Vue from 'vue'

// FontAwesome: import core, icon component, and one icon
import { library } from '@fortawesome/fontawesome-svg-core'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import { faPencil, faCircleCheck, faHandPointUp, faTrash } from '@fortawesome/free-solid-svg-icons'

// below imports are from local files (see the directory structure)
import App from './App.vue'
import router from './router'
import store from './store'

axios.defaults.withCredentials = true; // use credentials to allow session cookie to be sent to server
axios.defaults.baseURL = 'http://localhost:5001'; // this is the URL of the backend

// Prevent the production tip (i.e. welcome message) on Vue startup
Vue.config.productionTip = false;

// add icons to the library and then register the component globally
library.add(faPencil, faCircleCheck, faHandPointUp, faTrash);
Vue.component('font-awesome-icon', FontAwesomeIcon)

new Vue({
  router,
  store,
  render: h => h(App) // h is short for hyperscript, a function that creates virtual DOM nodes
}).$mount('#app')
