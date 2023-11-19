<template>
  <div>
    <hr>
    <table>
      <tr>
        <th>금융기관</th>
        <th>상품명</th>
        <th>6개월</th>
        <th>12개월</th>
        <th>24개월</th>
        <th>36개월</th>
      </tr>

      <template v-for="deposit in store.deposits">
        <tr>
          <td>{{ deposit.kor_co_nm }}</td>
          <td>{{ deposit.fin_prdt_nm }}</td>
          <td>{{ store.findSavingRate(deposit.depositoption_set, '6') }}</td>
          <td>{{ store.findSavingRate(deposit.depositoption_set, '12') }}</td>
          <td>{{ store.findSavingRate(deposit.depositoption_set, '24') }}</td>
          <td>{{ store.findSavingRate(deposit.depositoption_set, '36') }}</td>
        </tr>
      </template>
    </table>
  </div>
</template>

<script setup>
import { productStore } from '@/stores/productStore'
import { onMounted } from 'vue'

const store = productStore()

onMounted(() => {
  axios({
    url: `${API_URL}/products/deposits/`,
    method: 'get'
  })
    .then(res => {
      console.log(res.data)
      deposits.value = res.data
    })
    .catch(err => {
      console.log(err)
    })
})

</script>

<style scoped>

</style>