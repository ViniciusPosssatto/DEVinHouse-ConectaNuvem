import { createRouter, createWebHashHistory } from 'vue-router'



import MyHome from '@/components/views/home/MyHome.vue'
import CadasTro from '@/components/views/pessoas/cadastro/CadasTro.vue'
import ListaGem from '@/components/views/pessoas/listagem/ListaGem.vue'
import LoginUser from '@/components/views/login/LoginUser.vue'

const routes = [
    { path: '/', alias: ['/home', '/main' ], component: MyHome },
    { path: '/pessoas/cadastro', component: CadasTro },
    { path: '/pessoas/listagem', 
        component: ListaGem,
        beforeEnter: (to) => {
            const auth = localStorage.getItem('autenticado');
            if(auth){
                return true
            }
            return to = '/login';
        }
    
    },
    { path: '/login', 
        component: LoginUser,
        beforeEnter: (to) => {
            const login = localStorage.getItem('autenticado');
            if(login) {
                return to = '/'; 
            }
            return true;
        } 
    }    
]

const router = createRouter({
    routes,
    history: createWebHashHistory()    
});

export default router;