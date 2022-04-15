<template>
    <h3>Meu nome é: {{ sobreNome }}.</h3>
</template>

<script>
 export default {
     name: 'segundoComponente',
     data() {
         return {
             sobreNome: 'Ainda não sei'
         }
     },
     created() {
      this.sobreNome = "outra coisa"
    }
 }
</script>