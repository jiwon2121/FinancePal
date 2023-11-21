<template>
  <div>
    <h1>ProfileView</h1>
    <h3>{{ profile.nickname }}님의 프로필</h3>
    <p>생일 : {{ profile.birth_date }}</p>
    <p>email : {{ profile.email }}</p>
    <p>first name: {{ profile.first_name }}</p>
    <p>last name: {{ profile.last_name }}</p>
  </div>
</template>

<script setup>
import axios from 'axios'
import { ref } from 'vue'
import { useRoute } from 'vue-router'

const route = useRoute()
const profile = ref(null)

axios({
  method: 'get',
  url: `http://127.0.0.1:8000/profile/${route.params.username}/`
})
  .then(res => {
    profile.value = res.data
  })
  .catch(err => {
    console.log(err)
  })

</script>

<style scoped>

</style>