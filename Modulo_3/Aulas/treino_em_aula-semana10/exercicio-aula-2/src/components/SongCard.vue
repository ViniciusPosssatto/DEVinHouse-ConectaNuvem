<template>
  <div class="container" @click="onClickMusic">
    <div>{{ index }}</div>
    <img class="image" :src="imageUrl" />
    <div>
      <div :class="{ 'is-current': isActive }">{{ title }}</div>
      <div class="subtitle">{{ plays }}</div>
    </div>
  </div>
</template>

<script setup>
export default {
  name: "SongCard",
  props: {
    index: Number,
    imageUrl: String,
    title: String,
    plays: String,
    isActive: Boolean,
  },
  methods: {
    onClickMusic() {
      this.$emit("click-music-card", this.index);
    },
  },
};
</script>

<style scoped>
.container {
  width: 220px;
  background-color: #111;
  padding: 8px 16px;
  border-radius: 4px;

  display: flex;
  gap: 16px;
  align-items: center;
  color: white;
}

.container:hover {
  opacity: 0.9;
  cursor: pointer;
}

.image {
  height: 40px;
  width: 40px;
}

.subtitle {
  color: #999;
  margin-top: 8px;
}

.is-current {
  color: green;
}
</style>