import { createStore } from 'vuex'

const store = createStore({
    modules: {},
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
});

export default store;