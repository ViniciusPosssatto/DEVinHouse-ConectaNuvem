<template>
<main>
  <div class="row">
  <div class="inputbox">
    <label for="cep">CEP</label>
    <input id="cep" type="number" v-model="cepp" placeholder="Apenas números" required>
    <input class="btn-buscar" type="button" value="Buscar" @click="buscar">
  </div>
  <div class="inputbox">
    <label for="endereco">Endereço</label>
    <input type="text" id="endereco" v-model="logradouro" required>
  </div>
    <div class="inputbox">
      <label for="bairro">Bairro</label>
      <input type="text" id="bairro" v-model="bairro" required>
    </div>
    <div class="inputbox">
      <label for="cidade">Cidade</label>
      <input type="text" id="cidade" v-model="localidade" required>
    </div>
    <div class="inputbox">
      <label for="estado">Estado</label>
      <input type="text" id="estado" v-model="uf" required>
    </div>
    <div class="row">
      <button class="salvar" @click="salvado">Salvar</button>
    </div>
    
  </div>
  <p v-show="objeto">O CEP não existe no sistema! Verifique e tente novamente!</p>
</main>
</template>

<script>

export default {
  name: 'ViaCep',
 
  data() {
    return{
      cepp: '',
      bairro: null,
      logradouro: null,
      localidade: null,
      uf: null,
      objeto: false,
      
    }
  },
  methods: {
    async buscar(){
      try {
  
        const url = `http://viacep.com.br/ws/${this.cepp}/json`;
        
          const resposta = await fetch(url);
          //console.log(resposta);
          const conteudo = await resposta.json();
          //console.log(conteudo);
       
        this.localidade = conteudo.localidade;
        //console.log(this.localidade)
        this.uf = conteudo.uf;
        //console.log(this.uf)
        this.bairro = conteudo.bairro;
        //console.log(this.bairro)
        this.logradouro = conteudo.logradouro;
        //console.log(this.logradouro)
        this.objeto = conteudo.erro;
        //console.log(this.objeto)
        
      } catch (erro) {
          alert('O CEP deve conter 8 dígitos! Verifique e tente novamente')
      }
      
    },
    salvado(){
      if(this.cepp == ''){
        alert('Precisa preencher o formulário!')
      }else{
        alert('Cadastro salvo!')
      location.reload();
      }
    },
  }
}
</script>

<style>
.salvar{
  width: 200px;
  justify-self: center;
  height: 50px;
  border:none;
  outline: none;
  cursor: pointer;
  background-color: #EBCE07;
  font-size: 20px;
  font-weight: bold;
  border-radius: 6px;
}
.btn-buscar{
  width: 65px;
  justify-self: center;
  border:none;
  outline: none;
  cursor: pointer;
  background-color: #EBCE07;
  border-radius: 6px;
  padding: 3px 5px;
}
p{
  margin: 20px 0 0 0;
  color: #f80606;

}
</style>