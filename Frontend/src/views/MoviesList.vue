<template>
    <div class="py-6 d-flex flex-column justify-space-around h-screen">

        <h1 class="text-center">Movies List</h1>
        <v-container  class="d-flex flex-column  w-50 my-auto">
            <v-card v-for="film in films" :to="`/${film.id}`" :key="film.id" class="ma-4 pa-2 text-center">
                <v-card-title>{{ film.title }}</v-card-title>
            </v-card>
        </v-container>
        <v-pagination v-model="currentPage" class="mx-auto"  :length="store.state.pages" @click="fetchPage"></v-pagination>
    </div>
</template>
<script setup>
import { computed, ref } from 'vue';
import { useStore } from 'vuex'

    const store=useStore()
    const films=computed(()=>{
        return store.state.films[currentPage.value-1]
    })
    const currentPage=ref(1)
    const fetchPage=()=>{
        store.dispatch('fetchFilms',currentPage.value)
        store.commit('setCurrentPage',currentPage.value)
    }
</script>
