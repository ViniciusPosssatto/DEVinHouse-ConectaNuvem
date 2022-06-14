<template>
  <div id="app">
    <p>Exercício 1</p>
    <h1 v-text="msg"></h1>
    <p>v-model - irá alterar todos os campos que possuem a variável "msg" linkada.</p>
    <input type="text" v-model="msg">
    <hr>
    <br>
    <p>Exercício 2</p>
    <p>v-bind - irá alterar apenas o campo, sem alterar a variável.</p>
    <input type="text" :value="msg">
    <hr>
    <br>
    <p>Exemplo = v-model.lazy</p>
    <p>v-model.lazy - altera o valor da variável assim que clicar fora do campo de input.</p>
    <input type="text" v-model.lazy="msg">
    <hr>
    <br>
    <p>Exemplo = v-model.number</p>
    <p>v-model.number:string - testa se o campo input é string ou number e já converte para ser usado posterior (o teste está no console). Como é v-model, ele altera o valor da variável.</p>
    <label for=""> -- {{ typeof msg }} --</label>
    <input type="text" v-model.number="msg">
    <button @click="converte">Converter</button>
    <hr>
    <br>
    <p>Exercício 3</p>
    <p> v-html - insere uma tag Html através de uma variável (neste caso insere uma tag h6 e uma img com src via link e um width pré-definido).</p>
    <p v-html="html"></p>
    <hr>
    <br>
    <p>Exercício 4</p>
    <label for="" :class="colorLabel">Altera a cor do label digitando o nome da cor no input:</label>
    <br>
    <input type="text" v-model="colorLabel">
    <hr>
    <br>
    <p>Exercício 5</p>
    <label :class="mudaCor" for="">Alterar a cor deste texto através dos botões</label>
    <br>
    <button class="btn-red" @click="btnRed">Cor Vermelha</button>
    <button class="btn-blue" @click="btnBlue">Cor Azul</button>
    <button class="btn-green" @click="btnGreen">Cor Verde</button>
  </div>
</template>

<script>
export default {
  name: 'app',
  data() {
    return {
      colorLabel: '',
      msg: 'Bem vindo!',
      mudaCor: '',
      html: "<html><body><h6>Banner Exemplo</h6><img src='https://softauthor.com/wp-content/uploads/2020/04/create-a-banner-hero-unit-in-css-1-1024x365.png' style='width:300px'/></body></html>"
    }
  },
  methods: {
    trocarMensagem(){
      this.msg = 'outra mesangem'
    },
    converte(){
      console.log(Number(this.msg))
    },
    btnRed(){
      this.mudaCor = 'colorRed'
    },
    btnBlue(){
      this.mudaCor = 'colorBlue'
    },
    btnGreen(){
      this.mudaCor = 'colorGreen'
    }
  }
}
</script>

<style>
body{
  margin-left: 30px;
  background-color: rgb(189, 188, 188);
}
.colorRed{
  color: red;
  font-size: 20px;
}
.colorBlue{
  color: blue;
  font-size: 18px;
}
.colorGreen{
  color: green;
  font-size: 15px;
}
.btn-red{
  background-color: red;
}
.btn-blue{
  background-color: blue;
  color: white;
}
.btn-green{
  background-color: green;
}
button{
  width: 100px;
  height: 25px;
}
.blue{
  color: blue;
}
.red{
  color: red;
}
.green{
  color: green
}

</style>