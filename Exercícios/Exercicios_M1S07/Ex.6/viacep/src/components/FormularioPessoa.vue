<template>
  <div>
       <form>
        <div class="mb-3">
          <label for="exampleInputEmail1" class="form-label">Nome</label>
          <input type="email" v-model="nome" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp">
      
        </div>
        <div class="mb-3">
          <label for="exampleInputPassword1" class="form-label">Idade</label>
          <input type="number" v-model="idade" class="form-control" id="exampleInputPassword1">
        </div>
       
      </form>
  {{ idade }} {{ nome }}
  </div>
</template>

<script>
export default {
    name: 'FormularioPessoa',
    data(){
    return{
        nome: "",
        idade: ""
    }
  }
}
</script>

<style>

</style>