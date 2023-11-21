<template>
  <div>
    <h1>{{ profile.nickname }}님의 프로필</h1>
    <p>생일 : {{ profile.birth_date }}</p>
    <p>이메일 : {{ profile.email }}</p>
    <p>이름: {{ profile.first_name }}{{ profile.last_name }}</p>
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