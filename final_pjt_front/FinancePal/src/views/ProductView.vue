<template>
  <div>
    <h1>ProductView</h1>
    <ProductDeposits />
  </div>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
import ProductDeposits from '@/components/ProductDeposits.vue'
import ProductSavingS from '@/components/ProductSavingsS.vue'
import ProductSavingF from '@/components/ProductSavingsF.vue'
</script>

<style scoped>

</style>