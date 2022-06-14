<template>
    <div class="mt-5 center container" >
        <div v-if="titulo !== ''">
            <p>Mostrando componente</p>
            <h2 v-text="titulo"></h2>
        </div>
        <div style="border: 1px green;" class="center container" >
            <input type="text" v-model="titulo">
        </div>
    </div>
      
      
  
  
</template>

<script>
export default {
    data(){
        return {
            titulo: ''
        }
    }
}
</script>

<style>

</style>