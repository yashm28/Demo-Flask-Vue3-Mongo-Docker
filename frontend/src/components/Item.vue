<template>
  <div class="item">
    <b-card
    :title="title"
    :img-src="url"
    img-alt="Image"
    img-top
    tag="article"
    style="max-width: 20rem;"
    class="mb-2"
  >
  {{ count }}
  <b-button href="#" variant="primary" class="right">+</b-button>
  </b-card>
  </div>
</template>

<script setup lang="ts">
import { toRefs, withDefaults } from 'vue'
import type Post from '@/types/Post'

const post = withDefaults(defineProps<{
    title: string,
    count: number,
    url: string,
}>(), { title: "Title", count: 0, url: "https://picsum.photos/600/300/?image=25" });
const { title, count, url } = toRefs(post);

</script>

<style scoped>
.item {
  margin-top: 2rem;
  display: flex;
}
.right {
  float: right;
}
</style>
