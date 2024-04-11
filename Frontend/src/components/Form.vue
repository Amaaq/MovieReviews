<template>

    <v-form label="Update Movie Details"  class="pa-5 bg-white">
        <v-text-field v-model="formData.selectedDescription" label="Description"></v-text-field>
        <v-select
        v-model="formData.selectedActors"
        :items="store.state.actors"
        :item-props="itemProps"
        item-value="id"
        label="Actor"
        multiple
        ></v-select>
        <v-btn @click.prevent="$emit('handleSubmit',formData)">SUBMIT CHANGES</v-btn>
    </v-form>

</template>

<script setup>

import { defineProps, defineEmits,reactive } from 'vue'

import { useStore } from 'vuex'

const store=useStore()

defineEmits(['handleSubmit'])

const props= defineProps({
    description:{
        type: String,
    },
    actors:{
        type: Array
    }
})

const itemProps=(item)=>{
    return {
        title:item.last_name,
        subtitle:item.first_name
    }
}

const formData=reactive({
    selectedDescription: props.description,
    selectedActors: props.actors.map(actor=>actor.id)
})

</script>