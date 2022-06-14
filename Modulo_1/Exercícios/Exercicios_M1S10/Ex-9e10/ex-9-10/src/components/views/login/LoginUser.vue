<template>
    <div class="container">
        <div class="row">
            <div class="col-12">
                <label for="">E-mail</label>
                <input type="email" class="formcontrol">
            </div>
            <div class="col-12">
                <label for="">Senha</label>
                <input type="password" class="formcontrol">
            </div>
            <div class="col-12">
                <button class="btn btn-primary" @click="autenticar()">Login</button>
            </div>
        </div>
    </div>
</template>
<script>
export default {
    data() {
        return {
            login: {}
        }
    },
    methods: {
        autenticar() {
            this.$store.commit('autenticacaoModule/autenticar', this.login)
            if(this.$store.state.auteticacaoModule.autenticado){
                this.$router.push('/pessoas/listagem');
            }
        }
    }
}
</script>

<style>

</style>