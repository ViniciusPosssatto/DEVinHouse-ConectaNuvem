<template>
  <div id="app">
    <div style="color: red; font=weight: bold;">
      <MyHeader />
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
