<template>
    <v-container class="text-center pa-5 bg-white">    
        <v-radio-group v-model="formData.grade" class="text-center" inline label="Grade the Movie">
            <v-radio label="0" value="0"></v-radio>
            <v-radio label="1" value="1"></v-radio>
            <v-radio label="2" value="2"></v-radio>
            <v-radio label="3" value="3"></v-radio>
            <v-radio label="4" value="4"></v-radio>
            <v-radio label="5" value="5"></v-radio>
        </v-radio-group>
        <v-btn @click="$emit('handleSubmit',formData)">ADD REVIEW</v-btn>
    </v-container>
</template>

<script setup>
import { defineEmits,reactive } from 'vue';
    const formData = reactive({
        grade: 0
    })
    defineEmits(['handleSubmit'])
</script>