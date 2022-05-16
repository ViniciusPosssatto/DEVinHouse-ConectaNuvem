<template>
  <div class="container mt-4">
      <div class="col-3">
            <vee-form  @submit="autenticar" :validation-schema="schema" v-slot="{ errors }">
                <h2 class="text-center mb-4 title-login">Faça login</h2>
                <div class="mb-3">
                    <label for="exampleInputEmail1" class="form-label">Email:</label>
                    <vee-field type="email" name="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" v-model="login.email"/>
                    <div id="emailHelp" class="form-text">We'll never share your email with anyone else.</div>
                    <span class="text-danger" v-text="errors.email" v-show="errors.email"></span>
                </div>
                <div class="mb-3">
                    <label for="exampleInputPassword1" class="form-label">password:</label>
                    <vee-field name="password" type="password" class="form-control" id="exampleInputPassword1" v-model="login.password"/>
                    <span class="text-danger" v-text="errors.password" v-show="errors.password"></span>
                </div>
                <div class="mb-3">
                    <small><a href="#">Esqueceu a senha?</a></small>
                </div>
                <button type="submit" class="btn btn-primary">Fazer login</button>
            </vee-form>
      </div>
  </div>
</template>

<script>
import { Form, Field } from 'vee-validate'
import './../registro/validate'

export default {
    components: {
        'vee-form': Form,
        'vee-field': Field
    },
    data() {
        const schema = {
            email: "required|email",
            password: "required"
        }
        return {
            schema,
            login: {},
            loader: {}
        }
    },
    methods: {
        autenticar() {
            this.loader = this.$loading.show();
            this.$store.dispatch('autenticaUser/autenticar', this.login)
                .then(() => {
                    //console.log(this.login)
                    this.$toast.success('Login efetuado com sucesso!', {
                        position: 'top'
                    });
                    this.loader.hide();
                    this.$router.push('/dash');
                })
                .catch((err) => {
                    console.log(err.message)
                    this.$toast.error('Algo de errado ocorreu!', {
                        position: 'top'
                    });
                });
        },
    }
}
</script>

<style>

</style>