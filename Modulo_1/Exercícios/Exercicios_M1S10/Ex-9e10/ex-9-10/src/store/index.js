import { createStore } from 'vuex'

const autenticacaoModule = {
    namespaced: true,
    state(){
        return {
            autenticado: false
        }
    },
    mutations: {
        autenticar(state, login) {
            if(login.email === 'teste@teste.com' && login.senha === '123'){
                localStorage.setItem('autenticado', true);
                state.autenticado = true;
            }
        },
        logout(state){
            localStorage.removeItem('autenticado');
            state.autenticado = false;
        }    
    }
}



const cadastros = {
    state(){
        return{
            cadastrados: []
        }
    },
    mutations: {
        addCadastro(state, pessoa){
            state.cadastrados.push(pessoa)
        },
        
        excluir(state, index){
           state.cadastrados.splice(index, 1)
        },
    },
    actions: {
        
    },
    getters: {

    }
}

const store = createStore({
    modules: {
        autenticacaoModule,
        cadastros
    }
});

export default store;