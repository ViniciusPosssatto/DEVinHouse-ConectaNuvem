<template>
  <div class="app">
    <div class="row">
      <div class="col-4">
        <label for="nome">Digite seu nome:</label>
        <input type="text" id="nome" v-model="nome">
      </div>
      <div class="col-4">
        <label for="idade">Data de nascimento</label>
        <input type="date" id="idade" v-model="nascimento">
      </div>
      <div class="col-4">
        <button @click="addPessoa" class="btn btn-sm btn-primary">Adiciona Pessoa</button>
      </div>
    </div>
    <div class="row">
      <div class="col-12">
        <transition name="tabela" mode="out-in">
          <table class="table" v-if="lista.length > 0">
            <thead>
              <tr>
                <th>Id</th>
                <th>Nome</th>
                <th>Idade</th>
                <th></th>
              </tr>
            </thead>
            <transition-group name="lista">
              <tr v-for="(p, index) in lista" :key="p.id">
                <td v-text="p.id"></td>
                <td v-text="p.nome"></td>
                <td v-text="p.nascimento"></td>
                <td>
                  <button class="btn btn-sm btn-danger" @click="excluirPessoa(index)">Excluir</button>
                </td>
              </tr>
            </transition-group>
          </table>
          <div class="aviso text-center" v-else>
            <span>Não há nada na lista!</span>
            <br>
            <p>Clique em adicionar pessoa para começar.</p>
          </div>
        </transition>
      </div>
    </div>
  </div>
</template>

<script>


export default {
  name: 'App',
  data(){
    return{
      nome: '',
      nascimento: '',
      lista: []
    }
  },
  methods: {
    addPessoa(){
      this.lista.push({
        "id": new Date().getTime(),
        "nome": this.nome,
        "nascimento": this.calculaIdade(this.nascimento)
      })
      console.log(this.lista)
      this.lista.sort((x, y) => {
        return x.nascimento - y.nascimento;  // ordena os itens da lista pela idade
      })
      this.nome = ''
      this.nascimento = ''
    },
    excluirPessoa(index){
      this.lista.splice(index, 1)
    },
    calculaIdade(data){
      let hoje = new Date().getTime()
      let Nascimento = new Date(data).getTime()
      console.log(new Date())
      let diferenca = Math.abs(hoje - Nascimento)
      let idade = Math.floor(diferenca / (1000 * 60 * 60 * 24 * 365))

      return idade
    }
  }
}
</script>

<style>
body{
  padding: 50px;
}
input{
  margin-left: 10px;
}
.aviso{
  color: red;
  font-size: 25px;
  margin-top: 50px;
}
p{
  font-size: 15px;
  color: black;
}
/*Primeiro estilo*/
.tabela-leave-to,
.tabela-enter-from{
  opacity: 0;
  font-size: 0px
}

/*Segundo estilo*/
.tabela-leave-from,
.tabela-enter-to{
  opacity: 1;
  font-size: 10px;
}

/*Funcionamento*/
.tabela-leave-active,
.tabela-enter-active{
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
