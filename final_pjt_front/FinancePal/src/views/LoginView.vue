<template>
  <div>
    <h1>Login</h1>
    <form @submit.prevent="logIn">
      <input type="text" v-model.tirm="username">
      <input type="password" v-model.trim="password">
      <input type="submit">
    </form>
  </div>
</template>

<script setup>
import {ref} from 'vue'
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