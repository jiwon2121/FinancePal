<template>
  <div>
    <h1>Login</h1>
    <form @submit.prevent="logIn">
      <input type="text" id="username" v-model.tirm="username" placeholder="아이디를 입력하세요">
      <br>
      <input type="password" id="password" v-model.trim="password" placeholder="비밀번호를 입력하세요">
      <br>
      <input type="submit">
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { accountStore } from '@/stores/accountStore'

const store = accountStore()
const username = ref(null)
const password = ref(null)

const logIn = function() {
  const payload = {
    username: username.value,
    password: password.value
  }
  store.logIn(payload)
}
</script>

<style>

</style>