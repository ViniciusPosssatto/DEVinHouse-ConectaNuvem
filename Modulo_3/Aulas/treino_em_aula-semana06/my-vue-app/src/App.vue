<template>
  <v-app>
    <v-main>
      <NewTemplate/>
    </v-main>
  </v-app>
</template>

<script>
import NewTemplate from './components/NewTemplate.vue'

export default {
  name: 'App',

  components: {
    NewTemplate,
  },

  data: () => ({
    //
  }),
}
</script>
