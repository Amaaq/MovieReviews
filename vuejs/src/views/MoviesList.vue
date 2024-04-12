<template>
  <div class="py-6 d-flex flex-column justify-space-around h-screen">
    <h1 class="text-center">
      Movies List
    </h1>
    <v-container class="d-flex flex-column  w-50 my-auto">
      <v-card
        v-for="movie in store.state.movies"
        :key="movie.id"
        :to="`/${movie.id}`"
        class="ma-4 pa-2 text-center"
      >
        <v-card-title>{{ movie.title }}</v-card-title>
      </v-card>
    </v-container>
    <v-pagination
      v-model="currentPage"
      :total-visible="store.state.numberOfPages"
      class="mx-auto"
      :length="store.state.numberOfPages"
      @click="fetchMovies"
    />
  </div>
</template>

<script setup>

import { ref,onBeforeMount } from 'vue';
import { useStore } from 'vuex'

const store=useStore()
const currentPage=ref(1)

const fetchMovies= async ()=>{
    await store.dispatch('fetchMovies',currentPage.value)
}
onBeforeMount(async ()=>{
    if(!store.state.movies.length){
        await store.dispatch('fetchMovies',currentPage.value)
    }
})

</script>
