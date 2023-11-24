<template>
  <div class="d-flex justify-content-center flex-column align-items-center">
    <div class="login-form d-flex flex-column">
      <h1 class="text-center">가입을 환영합니다.</h1>
      <button class="btn btn-success w-100" @click="goMain">로그인 페이지로</button>
    </div>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'

const router = useRouter()

const goMain = function() {
  router.replace({name: 'login'})
}
</script>

<style scoped>

</style>