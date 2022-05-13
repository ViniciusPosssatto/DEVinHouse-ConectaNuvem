import axios from 'axios';
import { createStore } from 'vuex';

const userModule = {
    namespaced: true,
    actions: {
        newUser(context, user) {
            const token = localStorage.getItem('token')
            axios.post('https://devinhouse-auth.herokuapp.com/api/v1/user', user, {
                headers: {
                    authorization: token
                }
            })
                .then((result) => {
                    console.log(result)
                })
                .catch((err) => {
                    console.log(err)
                })
        },
        getUser(context) {
            const id = localStorage.getItem('id');
            const token = localStorage.getItem('token')
            axios.get(`https://devinhouse-auth.herokuapp.com/api/v1/user/${id}`, {
                authorization: token
            }) .then((response) => {
                context.
            }) .catch((err) => {
                console.log(err)
            })
        }
    }
}

const autenticacaoModule = {
    namespaced: true,
    state() {
        return {
            autenticado:false
        }
    },
    mutations: {
       /* autenticar(state, login) {
            if (login.email === 'teste@teste.com' && login.senha === "123") {
                localStorage.setItem('autenticado', true);
                state.autenticado = true;
            }
        },*/
        logout(state) {
            //localStorage.removeItem('autenticado');
            localStorage.removeItem('token');
            state.autenticado = false;
        },
        isAutenticado(state){
            state.autenticado = localStorage.getItem('token') ? true : false;
        }    
    },
    actions: {
        autenticar(context, login) {
            return new Promise ((resolve, reject) => {
                axios.post('https://devinhouse-auth.herokuapp.com/api/v1/login', login)
                .then((response) => {
                    const token = response.data.token;
                    const id = response.data.details.id;
                    localStorage.setItem('token', token)
                    localStorage.setItem('id', id)
                    context.state.autenticado = true;
                    resolve();
                    //console.log(response)
                })
                .catch((err) => {
                    console.log(err)
                    reject();
                })
            })
        }
    }
}

const store = createStore({
    modules: {
        autenticacaoModule,
        userModule
    }
});

export default store;