<template>
  <div>
    <h1>ProductView</h1>
    <button @click="changeComponent(1)">정기예금</button>
    <button @click="changeComponent(2)">정기적금</button>
    <button @click="changeComponent(3)">자유적금</button>
    <ProductDeposits v-if="type === 1"/>
    <ProductSavingS v-if="type === 2"/>
    <ProductSavingF v-if="type === 3"/>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import ProductDeposits from '@/components/ProductDeposits.vue'
import ProductSavingS from '@/components/ProductSavingsS.vue'
import ProductSavingF from '@/components/ProductSavingsF.vue'

const type = ref(1)

const changeComponent = function (num) {
  type.value = num
}
</script>

<style scoped>

</style>