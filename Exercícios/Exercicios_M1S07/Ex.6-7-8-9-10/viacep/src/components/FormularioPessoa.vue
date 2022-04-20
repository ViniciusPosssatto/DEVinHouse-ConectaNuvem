<template>
  <div>
     <main class="container">
        <h1 class="title">Formulário</h1>
        <div class="row">
            <div class="inputbox">
                <label for="nome">Nome</label>
                <input type="text" id="nome" v-model="nome" required>
            </div>
            <div class="inputbox">
                <label for="email">Email</label>
                <input type="text" id="email" v-model="email" required>
            </div>
            <div class="inputbox">
                <label for="idade">Idade</label>
                <input type="number" id="idade" v-model="idade" required>
            </div>
        </div>
        <div class="row">
            <div class="inputbox">
                <ViaCep/>
            </div>
        </div>
    </main>
       
  </div>
</template>

<script>
import ViaCep from "./ViaCep.vue"
export default {
    name: 'FormularioPessoa',
    components: {
      ViaCep
    },
    data(){
    return{
      nome: '',
      email: '',
      idade: ''
    }
  }
}
</script>

<style>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: 'Poppins', sans-serif;
}
.container {
    display: flex;
    flex-direction: column;
    justify-content: center;
    width: 50%;
    padding: 30px;
    gap: 40px;
    border: 5px solid rgb(65, 63, 63);
    background-color: black;
}
.title {
    font-size: 40px;
    text-align: center;
    user-select: none;
    color: #EBCE07
}
.row {
    display: grid;
    gap: 40px;
}
.inputbox label {
    top:0;
    left: 10px;
    font-size: 20px;
    color: #EBCE07;
    cursor: text;
}
input{
  margin: 0 0 0 15px;
}

</style>