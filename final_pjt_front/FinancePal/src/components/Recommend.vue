<template>
  <div>
    <p>----예금----</p>
    <ul>
      <PortfolioProduct
        v-for="product in store.recommend.recommendations.deposits"
        :product="product"
        type="deposits"
      />
    </ul>
    <p>----적금-----</p>
    <ul>
      <PortfolioProduct
        v-for="product in store.recommend.recommendations.savings"
        :product="product"
        type="savings"
      />
    </ul>
  </div>
</template>

<script setup>
import { profileStore } from '@/stores/profileStore'
import PortfolioProduct from '@/components/PortfolioProduct.vue'

const store = profileStore()
console.log(store)
</script>

<style scoped>

</style>