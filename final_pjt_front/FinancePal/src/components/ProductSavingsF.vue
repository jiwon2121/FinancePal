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

      <template v-for="saving in store.savings">
        <tr>
          <td>{{ saving.kor_co_nm }}</td>
          <td>{{ saving.fin_prdt_nm }}</td>
          <td>{{ store.findSavingRate(saving.savingoption_set, '6', 'F')}}</td>
          <td>{{ store.findSavingRate(saving.savingoption_set, '12', 'F') }}</td>
          <td>{{ store.findSavingRate(saving.savingoption_set, '24', 'F') }}</td>
          <td>{{ store.findSavingRate(saving.savingoption_set, '36', 'F') }}</td>
        </tr>
      </template>
    </table>
  </div>
</template>

<script setup>
import { productStore } from '@/stores/productStore'

const store = productStore()


</script>

<style scoped>

</style>