<template>
  <div class="container mt-5">
    <h1>Novo usuário</h1>
    <form @submit.prevent="save">
        <div class="row">
            <div class="col-3">
                <label for="nome">Nome</label>
                <input type="text" class="form-control" v-model="user.name">
            </div>
            <div class="col-3">
                <label for="email">E-mail</label>
                <input type="email" class="form-control" v-model="user.email">
            </div>
            <div class="col-3">
                <label for="senha">Senha</label>
                <input type="password" class="form-control" v-model="user.password">
            </div>
            <div class="col-12 mt-2">
                <button type="submit" class="btn btn-primary">Save</button>
            </div>
        </div>
    </form>
  </div>
</template>

<script>
export default {
    data() {
        return {
            user: {}
        }
    },
    methods: {
        save(){
            this.$store.dispatch('userModule/newUser', this.user)
        }
    }
}
</script>

<style>

</style>