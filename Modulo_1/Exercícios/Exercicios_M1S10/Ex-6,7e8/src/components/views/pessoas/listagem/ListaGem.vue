<template>
  <div class="listagem">
    <h1>Listagem!</h1>
    <div class="row">
      <div class="col-12">
        
          <table class="table" v-if="this.$store.state.cadastrados.length > 0">
            <thead>
              <tr>
                <th>Id</th>
                <th>Nome</th>
                <th>Data de nascimento</th>
                <th></th>
              </tr>
            </thead>
              <tr v-for="(p, index) in this.$store.state.cadastrados" :key="p.id">
                <td v-text="p.id"></td>
                <td v-text="p.nome"></td>
                <td v-text="p.nascimento"></td>
                <td>
                  <button class="btn btn-sm btn-danger" @click="excluirPessoa(index)">Excluir</button>
                </td>
              </tr>
          </table>
          <div class="aviso text-center" v-else>
            
            <span>Não há nada na lista!</span>
          </div>
        
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data(){
    return {
    }
  },
  methods: {
    getStore() {
      return this.$store.state.cadastrados;
    },
    excluirPessoa(index){
      this.$store.commit('excluir', index)
    }
  }
}
</script>

<style>

</style>