<template>
 <div class="app">
    <NavBar />
    <router-view></router-view>

 </div>
</template>

<script>
import NavBar from "./components/shared/navbar/NavBar.vue"
export default {
  name: 'App',
  components: {
    NavBar
}
}
</script>

<style>


</style>
