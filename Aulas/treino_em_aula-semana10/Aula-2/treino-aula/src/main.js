import { createApp } from 'vue'
import App from './App.vue'
import MyHome from '@/components/views/MyHome.vue'; 
import MyCadastro from "@/components/cadastro/MyCadastro.vue";
import NewUsuario from "@/components/cadastro/usuarios/NewUsuario.vue"

import { createRouter, createWebHashHistory } from 'vue-router'

const routes = [
    { path: '/', component: MyHome, alias: ["/home", "/main"], beforeEnter: (to, from) => {
        if(from.fullPath === "/cadastro/usuario"){
            return to.fullPath = "/cadastro"
        }
    } },
    {path: '/cadastro', component: MyCadastro, children: [
        {path: 'usuario', component: NewUsuario}
    ] }
];

const router = createRouter({
    routes,
    history: createWebHashHistory()
})

router.beforeEach((to, from) => {
    console.log("To:" + to.fullPath)
    console.log("From:" + from.fullPath)
    return true;
})
    
const app = createApp(App);

app.use(router)

app.mount('#app')
