<template>
    <div class="container">
        <h1>Home!</h1>
        <div class="row" v-if="autenticado">
            <div class="col-2" >
                <a href="#" @click="logout">Logout</a>
            </div>
            <div class="col-2">
                <router-link to="/reserva/nova">Nova Reserva</router-link>
            </div>
            <div class="col-2">
                <router-link to="/reserva/lista">Listar Reservas</router-link>
            </div>
            <div class="col-2">
                <router-link to="/user">Novo usuário</router-link>
            </div>
        </div>
        <div class="row" v-else>
            <div class="col-2" >
                <router-link to="/auth">Login</router-link>
            </div>
        </div>
        {{ user }}
    </div>
</template>
<script>
    export default {
        methods: {
            logout() {
                this.$store.commit('autenticacaoModule/logout');
                this.$router.push('/')
            }
        },
        computed: {
            autenticado() {
                return this.$store.state.autenticacaoModule.autenticado;
            },
            user() {
                return this.$store.state.userModule.user;
            }
        },
        mounted() {
            //this.$store.state.autenticacaoModule.autenticado = localStorage.getItem('autenticado');
            this.$store.state.autenticacaoModule.autenticado = localStorage.getItem('token') ? true : false;
        },
    }
</script>
<style>
</style>