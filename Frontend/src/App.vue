<template>
  <v-app >
    <RouterView />
  </v-app>
</template>

<script setup>

import { RouterView } from 'vue-router';
import { onBeforeMount } from 'vue';
import { useStore } from 'vuex'

const store=useStore()
onBeforeMount(()=>{
    store.dispatch('fetchFilms',1)
    store.dispatch('fetchActors')
})

</script>
