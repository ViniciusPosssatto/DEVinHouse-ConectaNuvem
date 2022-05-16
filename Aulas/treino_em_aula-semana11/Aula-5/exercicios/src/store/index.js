//import axios from 'axios';
import { createStore } from 'vuex';
import axios from 'axios'
import { isAutenticado, logout } from './mutations';



const userModule = {
    namespaced: true,
    state() {
        return {
            user: {}
        }
    },
    actions: {
        newUser(context, user){
            //const token = localStorage.getItem('token')
            axios.post('https://6279994273bad506857ad40c.mockapi.io/api/v1/users', user)
            .then((response) => {
                console.log(response)
            })
            .catch((err) => {
                console.log(err)
            })
        },
        getUser(context){
            const id = localStorage.getItem('id');
            const token = localStorage.getItem('token');
            axios.get(`https://devinhouse-auth.herokuapp.com/api/v1/user/${id}`, {
                authorization: token
            }).then((response) => {
                context.state.user = response.data
            }).catch((err) => {
                console.log(err);
            })
        }
    },
    getters: {

    },
    mutations: {

    }
}

const autenticaUser = { 
    namespaced: true,
    state() {
        return {
            autenticado: false
        }
    },
    mutations: {
        isAutenticado,
        logout 
    },
    actions: {
        autenticar(context, login) {
            return new Promise((resolve, reject) => {
                axios.post('https://devinhouse-auth.herokuapp.com/api/v1/login', login)
                    .then((response) => {
                        const token = response.data.token;
                        const id = response.data.details.id;
                        localStorage.setItem('token', token);
                        localStorage.setItem('id', id);
                        context.state.autenticado = true;
                        resolve();
                    })
                    .catch((err) => {
                        console.log(err);
                        reject();
                    })
            })
        }
    },
}

const store = createStore({
    modules: {
        userModule,
        autenticaUser
    }
});

export default store;