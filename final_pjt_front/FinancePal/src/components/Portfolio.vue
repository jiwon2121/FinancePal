<template>
  <div v-if="store.profile" class="mt-4 mt-3 mb-5">
  <h1 class="text-center">📊 {{ store.profile.nickname }}님의 포트폴리오</h1>
  <hr>
  <div class="row">
    <div class="col-3">
      <ul class="list-group">
        <li class="list-group-item p-0">
          <div class="row">
            <div class="col-3 ms-2">
              <p class="text-center mt-3">잔고</p>
            </div>
            <div class="col-8">
              <p class="mt-3 text-end overflow-x-hidden">
                {{ store.profile.balance.toLocaleString() + " 원" }}
              </p>
            </div>
          </div>
        </li>
        <li class="list-group-item p-0">
          <div class="row">
            <div class="col-3 ms-2">
              <p class="text-center mt-3">연봉</p>
            </div>
            <div class="col-8">
              <p class="mt-3 text-end overflow-x-hidden">
                {{ store.profile.salary.toLocaleString() + " 원" }}
              </p>
            </div>
          </div>
        </li>
      </ul>
    </div>
    
    <div class="col-9 row">
      <div class="col-6">
        <table class="table table-striped">
          <thead>
            <tr class="text-center">
              <th class="col">예금</th>
            </tr>
          </thead>
          <tbody class="table-group-divider">
            <PortfolioProduct
              v-for="product in store.profile.deposit_products"
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
              <th class="col">적금</th>
            </tr>
          </thead>
          <tbody class="table-group-divider">
            <PortfolioProduct
              v-for="product in store.profile.saving_products"
              :product="product"
              type="savings"
            />
            </tbody>
          </table>
        </div>
      </div>
    </div>
  <div class="border rounded p-5 mt-5 d-flex justify-content-center align-items-center flex-column">
    <h4>가입 상품 금리 비교 그래프</h4>
    <Chart
      :size="{ width: 600, height: 520 }"
      :data="prdt"
      :margin="margin"
      :direction="direction"
      :axis="axis">
  
      <template #layers>
        <Grid strokeDasharray="2,2" />
        <Bar :dataKeys="['상품명', '저축금리']" :barStyle="{ fill: '#19A7CE' }" />
        <Bar :dataKeys="['상품명', '최고우대금리']" :barStyle="{ fill: '#146C94' }" />
      </template>
  
      <template #widgets>
        <Tooltip
          borderColor="#146C94"
          :config="{
            '저축금리': { color: '#19A7CE' },
            '최고우대금리': { color: '#146C94' },
          }"
        />
      </template>
    </Chart>
  </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { profileStore } from '@/stores/profileStore'
import { Chart, Grid, Bar, Marker, Tooltip } from 'vue3-charts'
import PortfolioProduct from '@/components/PortfolioProduct.vue'

const store = profileStore()



const prdt = ref([])

store.profile.deposit_products.forEach((value) => {
  const temp = {
    '상품명': value.fin_prdt_nm.length > 4? value.fin_prdt_nm.slice(0,3)+'...' : value.fin_prdt_nm,
    '저축금리': value.intr_rate.intr_rate__avg,
    '최고우대금리': value.intr_rate.intr_rate2__avg,
  }
  prdt.value.push(temp)
})

store.profile.saving_products.forEach((value) => {
  const temp = {
    '상품명': value.fin_prdt_nm.length > 4? value.fin_prdt_nm.slice(0,3)+'...' : value.fin_prdt_nm,
    '저축금리': value.intr_rate.intr_rate__avg,
    '최고우대금리': value.intr_rate.intr_rate2__avg,
  }
  prdt.value.push(temp)
})

const direction = ref('horizontal')
const margin = ref({
  left:0,
  top: 20,
  right: 20,
  bottom: 0
})

const axis = ref({
  primary: {
    type: 'band'
  },
  secondary: {
    domain: ['dataMin', 'dataMax+1'],
    type: 'linear',
    ticks: 8
  }
})

</script>

<style scoped>

</style>