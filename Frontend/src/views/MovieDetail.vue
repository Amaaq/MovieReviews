<template>
    <v-container class="pa-12">
                <v-card>
                    <v-card-title primary-title>
                        {{film.title}}
                    </v-card-title>
                    <v-card-subtitle>
                        Rating : {{ film.average }}
                    </v-card-subtitle>
                    <v-card-text >
                        {{film.description}}
                    </v-card-text>
                    <v-card-actions>
                        <v-btn @click="dialog=true">Update data</v-btn>
                        <v-btn @click="dialog2=true">Add Review</v-btn>
                    </v-card-actions>
                </v-card>
                
    <v-col>
        <v-list>
            <v-list-subheader>Actors</v-list-subheader>
            
            <v-list-item v-for="actor in film.actors" :key="actor.id" color="primary" variant="plain">
                <template v-slot:prepend>
                    <v-icon icon="mdi-account"></v-icon>
                </template>
                
                <v-list-item-title v-text="`${actor.first_name} ${actor.last_name}`"></v-list-item-title>
            </v-list-item>
        </v-list>
    </v-col>
<v-dialog v-model="dialog" class="w-50">
    <Form :description="film.description" @handle-submit="updateDetails"/>
</v-dialog>
<v-dialog v-model="dialog2" class="w-50">
    <Review @handle-submit="addReview"/>
</v-dialog>
</v-container>
</template>
<script setup>
import Form from '@/components/Form.vue'
import Review from '@/components/Review.vue'

import { computed, ref } from 'vue'
import { useStore } from 'vuex'
import {useRoute} from 'vue-router'
const store=useStore()
const route= useRoute()
const id = route.params.id

const film = computed(()=>{
    return store.state.films[store.state.currentPage-1].find(film=>film.id==id)
})

const dialog=ref(false)
const dialog2=ref(false)
const updateDetails= (description)=> {
    dialog.value=false
    store.dispatch('updateDetails',{id,description})
}
const addReview = (grade)=>{
    dialog2.value=false
    store.dispatch('addReview',{id,grade})
}

</script>