<template>
  <div class="playlist-container">
    <div v-for="(music, index) in musics" :key="index">
      <SongCard
        :index="index + 1"
        :title="music.title"
        :imageUrl="music.imageUrl"
        :plays="music.plays"
        :is-active="activeMusicIndex === index + 1"
        @click-music-card="onClickMusicCard"
      />
    </div>
  </div>
</template>

<script setup>
import SongCard from "./components/SongCard.vue";

export default {
  name: "App",
  components: {
    SongCard,
  },
  methods: {
    onClickMusicCard(param) {
      if (param === this.activeMusicIndex) {
        this.activeMusicIndex = null;
      } else {
        this.activeMusicIndex = param;
      }
    },
  },
  data() {
    return {
      activeMusicIndex: null,
      musics: [
        {
          imageUrl:
            "https://i.scdn.co/image/ab67706c0000bebb2d9a8ea5c10556cedffb6129",
          title: "LoFi Beats 1",
          plays: "3.456.789",
        },
        {
          imageUrl:
            "https://i1.sndcdn.com/avatars-g2x1wgHhB08StOUA-dGv2FA-t500x500.jpg",
          title: "LoFi Beats 2",
          plays: "7.964.147",
        },
        {
          imageUrl:
            "https://i1.sndcdn.com/avatars-g2x1wgHhB08StOUA-dGv2FA-t500x500.jpg",
          title: "LoFi Beats 3",
          plays: "7.964.147",
        },
        {
          imageUrl:
            "https://i1.sndcdn.com/avatars-g2x1wgHhB08StOUA-dGv2FA-t500x500.jpg",
          title: "LoFi Beats 4",
          plays: "7.964.147",
        },
      ],
    };
  },
};
</script>

<style scoped>
.pageContainer {
  display: flex;
  flex-direction: column;
  gap: 24px;
  margin-top: 24px;
}

.playlist-container {
  display: flex;
  flex-direction: column;
  gap: 16px;
}
</style>