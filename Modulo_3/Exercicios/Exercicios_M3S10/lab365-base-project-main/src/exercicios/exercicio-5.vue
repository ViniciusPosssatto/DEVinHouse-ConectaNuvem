<template>
  <div class="bg">
    <h1>TO do List</h1>
    <input type="text" placeholder="Digite um item" v-model="item" />
    <button @click="saveInList()">Insert</button>
    <div v-if="listaToDo.length === 0">
      <span>Nenhum conteúdo salvo</span>
    </div>
    <div>
      <ul v-for="(todo, index) in listaToDo" :key="index">
        <div class="inline">
          <li v-text="todo"></li>
          <button @click="deleteItemList(index)">remover</button>
        </div>
      </ul>
    </div>
  </div>
</template>

<script>
import { ref, reactive } from "vue";

export default {
  name: "ExercicioCinco",
  setup() {
    const listaToDo = reactive([]);
    let item = ref();
    function saveInList() {
      listaToDo.push(item.value);
      this.item = "";
    }
    function deleteItemList(item) {
      listaToDo.splice(item, 1);
    }
    return {
      listaToDo,
      item,
      saveInList,
      deleteItemList,
    };
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
.bg {
  background-color: #eee;
  padding: 64px 32px;
}
.inline {
  display: inline-flex;
  gap: 40px;
}
</style>
