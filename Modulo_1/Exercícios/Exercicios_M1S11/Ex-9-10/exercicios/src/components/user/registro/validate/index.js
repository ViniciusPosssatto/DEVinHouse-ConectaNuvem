import { defineRule } from 'vee-validate'

const required = defineRule("required", value => {
    if (!value || value.length === 0) {
        return "Campo obrigatório"
    }

    return true;
});

const validaSenha = defineRule("validaSenha", value => {
    if(this.senha1 !== value){
        return "As senhas não são iguais!"
    }
    return true;
});
const email = defineRule('email', value => {
    if (!value || !value.length) {
        return true;
    }
    // Checar se é email válido
    if (!/[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,4}/.test(value)) {
        return 'Coloque um email válido!';
    }
    return true;
});



export { required, email, validaSenha }