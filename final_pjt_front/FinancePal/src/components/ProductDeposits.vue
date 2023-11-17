<template>
  <div>
    <h1>정기예금</h1>
    <hr>
    <template v-for="deposit in deposits">
      <p>{{ deposit.kor_co_nm }} | {{ deposit.fin_prdt_nm }}</p>
      <hr>
    </template>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'

const deposits = ref(null)
axios({
  url: 'http://127.0.0.1:8000/products/savings/',
  method: 'get'
})
  .then(res => {
    console.log(res.data)
    deposits.value = res.data
  })

</script>

<style scoped>

</style>