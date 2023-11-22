<template>
  <div>
    포트폴리오
  </div>
  <p>잔고: {{ store.profile.balance }}</p>
  <p>연봉: {{ store.profile.salary }}</p>
  <p>가입 상품</p>
  <div>
    <p>----예금----</p>
    <ul>
      <PortfolioProduct
        v-for="product in store.profile.deposit_products"
        :product="product"
        type="deposits"
      />
    </ul>
    <p>----적금-----</p>
    <ul>
      <PortfolioProduct
        v-for="product in store.profile.saving_products"
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


</script>

<style scoped>

</style>