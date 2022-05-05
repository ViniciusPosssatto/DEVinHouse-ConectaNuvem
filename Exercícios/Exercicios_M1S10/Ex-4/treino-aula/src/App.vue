<template>
  <div class="app">
    <button @click="addPessoa" class="btn btn-sm btn-primary">Adiciona Pessoa</button>
    <div class="row">
      <div class="col-12">
        <table class="table">
          <thead>
            <tr>
              <th>Id</th>
              <th>Nome</th>
              <th>Idade</th>
              <th></th>
            </tr>
          </thead>
          <transition-group name="lista">
            <tr v-for="p in pessoas" :key="p.id">
              <td v-text="p.id"></td>
              <td v-text="p.nome"></td>
              <td v-text="p.idade"></td>
              <td>
                <button class="btn btn-sm btn-danger" @click="excluirPessoa">Excluir</button>
              </td>
            </tr>
          </transition-group>
        </table>
      </div>
    </div>
  </div>
</template>

<script>


export default {
  name: 'App',
  data(){
    return{
      pessoas: [{
        id: 0,
        nome: 'pessoa 1',
        idade: 20
      },{
        id: 1,
        nome: 'pessoa 2',
        idade: 24
      }]
    }
  },
  methods: {
    // add(){
    //   this.lista.push(Number(this.numero));
    //   //this.lista.sort(); //o sort ordena a sequência dos números
    //   this.lista.sort((x, y) => {
    //     return x - y;  // nesse caso ele vai ordenar números maiores que 2 casas decimais
    //   })
    // }
    addPessoa(){
      this.pessoas.push({
        id: this.pessoas[this.pessoas.length - 1].id + 1,
        nome: "qualquer",
        idade: 21
      })
      this.pessoas.sort((x, y) => {
        return x.idade - y.idade;  // ordena os itens da lista pela idade
      })
    },
    excluirPessoa(index){
      this.pessoas.splice(index, 1)
    }
  }
}
</script>

<style>

/*Primeiro estilo*/
.header-leave-to,
.header-enter-from{
  /*background-color: white;*/
  opacity: 0;
  font-size: 0px
}

/*Segundo estilo*/
.header-leave-from,
.header-enter-to{
  /*background-color: black;*/
  opacity: 1;
  font-size: 2.5em;
}

/*Funcionamento*/
.header-leave-active,
.header-enter-active{
  /*transition: opacity 2s;*/
  transition: all 0.5s;
}


/*---- parte da Lista ------*/

/*Primeiro estilo*/
.lista-leave-to,
.lista-enter-from{
  opacity: 0;
}

/*Segundo estilo*/
.lista-leave-from,
.lista-enter-to{
  opacity: 1;
}

/*Funcionamento*/
.lista-move,
.lista-leave-active,
.lista-enter-active{
  transition: all 2s;
}
</style>
