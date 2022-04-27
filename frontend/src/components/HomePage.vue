<template>
  <b-card-group deck>
    <ul v-for="post in posts" :key="post.id">
      <Item :id="post.id" :title="post.title" :count="post.count" :url="post.url" @increment="id => increment(id)" @decrement="id => decrement(id)">
      </Item>
    </ul>
  </b-card-group>
</template>

<script setup lang="ts">
import Item from '@/components/Item.vue'
import type Post from '@/types/Post'
import { ref } from '@vue/reactivity'
import { onMounted } from 'vue'
import * as records from '@/data/db.json'

let posts = ref<Post[]>([
  { id: "1", title: "Title", count: 0, url: "https://picsum.photos/600/300/?image=25" },
  { id: "2", title: "Title1", count: 1, url: "https://picsum.photos/600/300/?image=25" },
  { id: "3", title: "Title2", count: 2, url: "https://picsum.photos/600/300/?image=25" },
  { id: "4", title: "Title3", count: 3, url: "https://picsum.photos/600/300/?image=25" },
]);

onMounted(async () => {
  console.log('test');
  try {
    let response = await fetch('http://localhost/backend/post/getall');
    let data = await response.json();
    if (data.posts.length == 0) {
      response = await fetch('http://localhost/backend/post/createall', {
        method: 'POST',
        headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(records),
      });
      data = await response.json();
    }
    posts.value = data.posts;
    console.log(posts);
  } catch (exception) {
    console.log(exception);
  }
});

const increment = async (id: string) => {
  const response = await fetch('http://localhost/backend/post/increment', {
    method: 'POST',
    headers: {
      'Accept': 'application/json',
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({'id': id }),
  });
  const data = await response.json();
  posts.value.forEach(post => {
    if (post.id === id) post.count = data.post.count;
  });
}

const decrement = async (id: string) => {
  const response = await fetch('http://localhost/backend/post/decrement', {
    method: 'POST',
    headers: {
      'Accept': 'application/json',
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({'id': id }),
  });
  const data = await response.json();
  posts.value.forEach(post => {
    if (post.id === id) post.count = data.post.count;
  });
}
</script>
