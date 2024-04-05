<template>
    <v-form  class="pa-5 bg-white">
            <v-text-field v-model="selectedDescription" label="Description"></v-text-field>
            <v-btn @click.prevent="$emit('handleSubmit',selectedDescription)">SUBMIT CHANGES</v-btn>
    </v-form>
</template>
<script setup>
import { defineProps, defineEmits,ref } from 'vue';

defineEmits(['handleSubmit'])
const props= defineProps({
    description:{
        type: String,
    },
})
const selectedDescription=ref(props.description)
</script>