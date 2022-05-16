import { createRouter, createWebHashHistory } from 'vue-router'
/* eslint-disable */

// import componentes
import HomeView from '@/components/home/HomeView.vue'
import DashboardView from '@/components/dashboard/DashboardView.vue'
import LoginView from '@/components/user/login/LoginView.vue'
import RegisterView from '@/components/user/registro/RegisterView.vue'

const routes = [
    { 
        path: '/',
        alias: ['/home', '/main'],
        component: HomeView
    },
    {
        path: '/login',
        alias: ['/entrar'],
        component: LoginView,
        beforeEnter: (to) => {
            const auth = localStorage.getItem('token');
            if(auth) {
                return to = '/';
            }
            return true;
        }
    },
    {
        path: '/register',
        alias: ['/registrar', '/cadastrar'],
        component: RegisterView,
       
    },
    {
        path: '/dashboard',
        alias: ['/dash'],
        component: DashboardView,
        beforeEnter: (to) => {
            const auth = localStorage.getItem('token');
            if(auth) {
                return true;
            }
            return to = '/login'
        }
    }
]

const router = createRouter({
    routes,
    history: createWebHashHistory()
});

export default router;