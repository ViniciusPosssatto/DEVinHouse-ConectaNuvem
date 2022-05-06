import { createApp } from 'vue'
import App from './App.vue'
import { createRouter, createWebHashHistory } from 'vue-router'


import MyHome from '@/components/views/home/MyHome.vue'
import CadasTro from '@/components/views/pessoas/cadastro/CadasTro.vue'
import ListaGem from '@/components/views/pessoas/listagem/ListaGem.vue'

const routes = [
    { path: '/', alias: ['/home', '/main' ], component: MyHome },
    { path: '/pessoas/cadastro', component: CadasTro },
    { path: '/pessoas/listagem', component: ListaGem }    
]

const router = createRouter({
    routes,
    history: createWebHashHistory()    
});

const app = createApp(App);

app.use(router)

app.mount('#app')
