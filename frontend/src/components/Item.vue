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
      <span>{{ count }}</span>
      <b-button href="#" variant="primary" class="right" @click="$emit('increment', post.id)">+1</b-button>
      <b-button href="#" variant="danger" class="right" @click="$emit('decrement', post.id)" :disabled="post.count <= 0">-1</b-button>
    </b-card>
  </div>
</template>

<script setup lang="ts">
import { toRefs, withDefaults } from 'vue'
import type Post from '@/types/Post'

const post = withDefaults(defineProps<{
    id: string,
    title: string,
    count: number,
    url: string,
}>(), { id: "1", title: "Title", count: 0, url: "https://picsum.photos/600/300/?image=25" });
const { id, title, count, url } = toRefs(post);

</script>

<style scoped>
.item {
  margin-top: 2rem;
  display: flex;
  width: 100%;
  height: 20vw;
  object-fit: cover;
}
.right {
  float: right;
  margin: 2px;
}
.bottom {
  margin-bottom: 2px;
}

</style>
