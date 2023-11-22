<template>
  <div class="d-flex flex-column">
    <div class="text-center my-3">
      <h1 v-if="type===1" class="mb-3">💸 정기예금 상품 비교</h1>
      <h1 v-if="type===2" class="mb-3">💰 정기적금 상품 비교</h1>
      <h1 v-if="type===3" class="mb-3">💰 자유적금 상품 비교</h1>
    </div>
    <div>
      <button type="button" class="mx-1 btn btn-outline-dark" :class="{active:type==1}" @click="changeComponent(1)">정기예금</button>
      <button type="button" class="mx-1 btn btn-outline-dark" :class="{active:type==2}" @click="changeComponent(2)">정기적금</button>
      <button type="button" class="mx-1 btn btn-outline-dark" :class="{active:type==3}" @click="changeComponent(3)">자유적금</button>
    </div>
    <ProductDeposits v-if="type === 1"/>
    <ProductSavingS v-if="type === 2"/>
    <ProductSavingF v-if="type === 3"/>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
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