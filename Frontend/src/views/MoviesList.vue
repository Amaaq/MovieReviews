<template>
    <v-card v-for="film in films">
        {{ film.title }}
    </v-card>
</template>
<script setup>
    import { computed, ref } from 'vue';
import { useStore } from 'vuex'

    const store=useStore()
    const films=computed(()=>{
        return store.state.films[currentPage.value-1]
    })
    const currentPage=ref(1)
</script>
