<template>
  <div v-if="store.recommend" class="mt-4 mt-3 mb-5">
    <h1 class="text-center">👍 {{ store.profile.nickname }}님을 위한 금융 상품 추천</h1>
    <hr>
    <div class="row mt-5">
      <div class="col-6">
        <table class="table table-striped">
          <thead>
            <tr class="text-center">
              <th class="col">예금 상품</th>
            </tr>
          </thead>
          <tbody class="table-group-divider">
            <PortfolioProduct
              v-for="product in store.recommend.recommendations.deposits"
              :product="product"
              type="deposits"
            />
          </tbody>
        </table>
      </div>
      <div class="col-6">
        <table class="table table-striped">
          <thead>
            <tr class="text-center">
              <th class="col">적금 상품</th>
            </tr>
          </thead>
          <tbody class="table-group-divider">
            <PortfolioProduct
              v-for="product in store.recommend.recommendations.savings"
              :product="product"
              type="savings"
            />
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script setup>
import { profileStore } from '@/stores/profileStore'
import PortfolioProduct from '@/components/PortfolioProduct.vue'

const store = profileStore()
</script>

<style scoped>

</style>