import { createApp } from 'vue'
import App from './App.vue'

import { createStore } from 'vuex'

const store = createStore({
    modules: {},
    state(){
        return{
            display: 'Display',
            seconds: 0,
            actived: false
        }
    },
    mutations: { //métodos síncronos
        updateDisplay(state, valor){
            state.display = valor.toUpperCase()
        },
        parar(){
            state.actived = false;
        }
    },
    actions: { //métodos assíncronos
        startCron(context){
            if(context.state.actived) {
                setTimeout(() => {
                    context.state.seconds++;
                    context.dispatch('startCron') // o dispatch adiciona uma ação para o actions
                }, 1000);}
        }
    },
    getters: { //váriaveis computadas

    }
})

    
const app = createApp(App);

app.use(store)

app.mount('#app')
