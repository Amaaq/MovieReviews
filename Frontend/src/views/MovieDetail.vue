<template>
    <v-container v-if="movie" class="pa-12">
        <v-btn to="/" class="w-25 mb-5"
          prepend-icon="mdi-arrow-left-circle"
        >
         Movie List
        </v-btn>
        <v-card>
            <v-card-title primary-title> {{movie.title}} </v-card-title>
            <v-card-subtitle> Rating : {{ movie.average }} </v-card-subtitle>
            <v-card-text > {{movie.description}} </v-card-text>
            <v-card-actions>
                <v-btn @click="dialog=true">Update data</v-btn>
                <v-btn @click="dialog2=true">Add Review</v-btn>
            </v-card-actions>
        </v-card> 
        <v-list>
            <v-list-subheader>Actors</v-list-subheader>
            <v-list-item v-for="actor in movie.actors" :key="actor.id" color="primary" variant="plain">
                <template v-slot:prepend>
                    <v-icon icon="mdi-account"></v-icon>
                </template>
                <v-list-item-title v-text="`${actor.first_name} ${actor.last_name}`"></v-list-item-title>
            </v-list-item>
        </v-list>
        <v-dialog v-model="detailsDialog" class="w-50">
            <DetailsForm :description="movie.description" :actors="movie.actors" @handle-submit="updateDetails"/>
        </v-dialog>
        <v-dialog v-model="reviewDialog" class="w-50">
            <ReviewForm @handle-submit="addReview"/>
        </v-dialog>
    </v-container>
<v-container v-else>Loading ...</v-container>
</template>

<script setup>


import { computed, onBeforeMount, ref } from 'vue'
import { useStore } from 'vuex'
import {useRoute} from 'vue-router'
import DetailsForm from '@/components/DetailsForm.vue';
import ReviewForm from '@/components/ReviewForm.vue';

const store=useStore()
const route= useRoute()


const movieId = route.params.id
const movie = computed(()=>{
    return store.state.selectedMovie
})


const detailsDialog=ref(false)
const reviewDialog=ref(false)
const updateDetails= async (formData)=> {
    detailsDialog.value=false
    await store.dispatch('updateDetails',{movieId,...formData})
}
const addReview = async(data)=>{
    reviewDialog.value=false
    await store.dispatch('addReview',{movieId,...data})
}


onBeforeMount(async ()=>{
    await store.dispatch('fetchMovieById',movieId)
    if(!store.state.actors.length){
        await store.dispatch('fetchActors')
    }
})

</script>