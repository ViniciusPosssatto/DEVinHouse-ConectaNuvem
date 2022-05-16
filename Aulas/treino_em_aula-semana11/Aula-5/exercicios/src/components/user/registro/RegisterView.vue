<template>
  <div class="container mt-4">
      <div class="col-3">
            <vee-form id="formUser" @submit="cadastrar" :validation-schema="schema" v-slot="{ errors }">
                <h2 class="text-center mb-4 title-login">Cadastre-se</h2>
                <div class="mb-3">
                    <label for="name" class="form-label">Nome:</label>
                    <vee-field type="text" name="name" class="form-control" id="name" v-model="user.name"/>
                    <span class="text-danger" v-text="errors.name" v-show="errors.name"></span>
                </div>
                <div class="mb-3">
                    <label for="exampleInputEmail1" class="form-label">Email:</label>
                    <vee-field type="email" name="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" v-model="user.email"/>
                    <span class="text-danger" v-text="errors.email" v-show="errors.email"></span>
                </div>
                <div class="mb-3">
                    <label for="exampleInputPassword1" class="form-label">Senha:</label>
                    <vee-field type="password" name="senha1" class="form-control" id="exampleInputPassword1" v-model="senha1"/>
                    <span class="text-danger" v-text="errors.senha1" v-show="errors.senha1"></span>
                </div>
                <div class="mb-3">
                    <label for="exampleInputPassword2" class="form-label">Repita a senha:</label>
                    <vee-field type="password" name="password" class="form-control" id="exampleInputPassword2" v-model="user.password"/>
                    <span class="text-danger" v-text="errors.password" v-show="errors.password"></span>
                </div>
                <button type="submit" class="btn btn-primary">Cadastrar</button>
            </vee-form>
      </div>
  </div>
</template>

<script>
import { Form, Field } from 'vee-validate'
import './validate'

export default {
    components: {
        'vee-form': Form,
        'vee-field': Field
    },
    data() {
        
        const schema = {
        name: "required",
        email: "required|email",
        senha1: "required",
        password: "required"
        }
        return {
            schema,
            user : {
                name: '',
                email: '',
                password: ''
            },
            senha1: ''
            
            
        }
    },
    
    methods: {
        cadastrar() {
            this.$store.dispatch('userModule/newUser', this.user);
            this.user = {};
            document.getElementById('formUser').reset();
            this.$toast.success('Cadastro efetuado com sucesso!', {
                position: 'top'
              });
            this.$router.push('/login');
        },
        
    }
}
</script>

<style>

</style>