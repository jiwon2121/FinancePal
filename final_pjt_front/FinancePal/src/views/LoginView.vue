<template>
  <div class="d-flex justify-content-center flex-column align-items-center">
    <div class="login-form d-flex flex-column">
      <h1 class="text-center">FinancePal</h1>
      <form @submit.prevent="logIn">
        <input class="form-control my-3" type="text" id="username" v-model.tirm="username" placeholder="아이디를 입력하세요">
        <input class="form-control my-3" type="password" id="password" v-model.trim="password" placeholder="비밀번호를 입력하세요">
        <button class="btn btn-success w-100">로그인</button>
      </form>
    </div>
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
.login-form {
  position: absolute;
  top: 30%;
}
</style>