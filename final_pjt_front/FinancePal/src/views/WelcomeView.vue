<template>
  <div>
    <h1>가입을 환영합니다.</h1>
    <button @click="goMain">메인으로</button>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'

const router = useRouter()

const goMain = function() {
  router.push({name: 'main'})
}
</script>

<style scoped>

</style>