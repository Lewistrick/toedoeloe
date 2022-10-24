import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Login from '../views/Login.vue'
import Register from '../views/Register.vue'
import Profile from '../views/Profile.vue'
import Todos from '../views/Todos.vue'
import AddTodo from '../views/AddTodo.vue'
import EditTodo from '../views/EditTodo.vue'
import store from '../store'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/register',
    name: 'Register',
    component: Register
  },
  {
    path: '/profile',
    name: 'Profile',
    component: Profile,
    meta: { requiresAuth: true }
  },
  {
    path: '/todos',
    name: 'Todos',
    component: Todos,
    meta: { requiresAuth: true }
  },
  {
    path: '/addtodo',
    name: 'AddTodo',
    component: AddTodo,
    meta: { requiresAuth: true }
  },
  {
    path: '/edittodo/:id',
    name: 'EditTodo',
    component: EditTodo,
    props: true,
    meta: { requiresAuth: true }
  },
]

// Create the router instance and pass the `routes` option
const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL, // this is the URL of the frontend
  routes
})

// check if the user is logged in before each route change
router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requiresAuth)) {
    store.dispatch('checkLogin');
    if (store.getters.isLoggedIn) {
      next();
      return;
    }
    //logout
    store.dispatch('logOut');
    next('/login');
  } else {
    next();
  }
});

export default router;
