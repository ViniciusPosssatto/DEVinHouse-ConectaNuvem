<template>
  <div>
      <nav class="nav navbar-dark bg-dark" v-if="autenticado"> 
          <router-link to="/home">Home</router-link>
          <router-link to="/dash">Dashboard</router-link>
          <a href="#" @click="logout">Logout</a>
      </nav>
      <nav class=" nav navbar-dark bg-dark" v-else>
          <router-link to="/register">Cadastrar-se</router-link>
          <router-link class="ms-4" to="/login">Login</router-link>
      </nav>
  </div>
</template>

<script>
  export default {
    methods: {
      logout() {
        this.$store.commit('autenticaUser/logout');
        this.$router.push('/');
      }
    },
    computed: {
      autenticado(){ 
        return this.$store.state.autenticaUser.autenticado;
      },
      user(){
        return this.$store.state.userModule.user;
      }
    },
    mounted() {
      this.$store.state.autenticaUser.autenticado = localStorage.getItem('token') ? true : false;
    }
  }

</script>

<style>
.nav{
  padding: 10px 20px;
  gap: 20px;
}
</style>