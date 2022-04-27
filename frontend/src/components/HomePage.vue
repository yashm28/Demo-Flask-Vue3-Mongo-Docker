<template>
  <ul v-for="post in posts" :key="post.id">
    <Item :title="post.title" :count="post.count" :url="post.url">
    </Item>
  </ul>
</template>

<script setup lang="ts">
import Item from '@/components/Item.vue'
import type Post from '@/types/Post'
import { ref } from '@vue/reactivity'
import { onMounted } from 'vue'

// const response = await fetch('http://localhost:5001/post/getall');
// console.log(response)

onMounted(async () => {
  console.log('test');
  const response = await fetch('http://localhost/backend/post/getall');
  console.log(response.json);
});

const posts = ref<Post[]>([
  { id: 1, title: "Title", count: 0, url: "https://picsum.photos/600/300/?image=25" },
  { id: 2, title: "Title1", count: 1, url: "https://picsum.photos/600/300/?image=25" },
  { id: 3, title: "Title2", count: 2, url: "https://picsum.photos/600/300/?image=25" },
  { id: 4, title: "Title3", count: 3, url: "https://picsum.photos/600/300/?image=25" },
]);
</script>
