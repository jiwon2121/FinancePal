<template>
<div class="main-text"></div>
<header class="masthead d-flex justify-content-center">
  <div class="mastbody container d-flex align-items-center flex-column">
    <h1 class="masthead-heading mb-5 fw-bold">
      FinancePal
    </h1>
    <button class="masthead-btn btn btn-lg fw-bold btn-light" @click="router.push({ path: 'product' })">시작하기</button>
  </div>
</header>
</template>

<script setup>
import { useRouter } from 'vue-router'
const router = useRouter()


</script>

<style scoped>
.masthead {
  position: absolute;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  background-color: #AFD3E2;
}
.mastbody {
  margin-top: 300px;
}
.masthead-heading {
  color: #146C94;
}
.masthead-btn {
  background-color: #F6F1F1;
  color: #146C94;
  border-color: #F6F1F1;
}
</style>