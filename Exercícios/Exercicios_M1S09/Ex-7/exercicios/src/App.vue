<template>
  <div id="app">
    <div style="color: red; font=weight: bold;">
      <MyHeader />
    </div>
     
     <div style="border: 1px green;">
        <input type="text" v-model="msg">
    </div>
   
  </div>
</template>

<script>
import MyHeader from "./assets/components/MyHeader.vue"
export default {
    name: "app",
    data() {
        return {
           msg: ''
        };
    },
    methods: {},
    components: { 
      MyHeader 
      }
}
</script>

<style>

</style>
