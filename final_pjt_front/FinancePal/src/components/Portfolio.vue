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