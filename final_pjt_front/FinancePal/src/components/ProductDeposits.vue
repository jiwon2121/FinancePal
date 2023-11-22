<template>
    <hr>
    <table class="table table-striped">
      <thead>
        <tr>
          <th>금융기관</th>
          <th>상품명</th>
          <th>6개월</th>
          <th>12개월</th>
          <th>24개월</th>
          <th>36개월</th>
        </tr>
      </thead>
      <tbody class="table-group-divider">
        <template v-for="deposit in store.deposits">
          <tr>
            <td>{{ deposit.kor_co_nm }}</td>
            <td>{{ deposit.fin_prdt_nm }}</td>
            <td>{{ store.findSavingRate(deposit.depositoption_set, '6') }}</td>
            <td>{{ store.findSavingRate(deposit.depositoption_set, '12') }}</td>
            <td>{{ store.findSavingRate(deposit.depositoption_set, '24') }}</td>
            <td>{{ store.findSavingRate(deposit.depositoption_set, '36') }}</td>
            <td>
              <button type="button" class="btn btn-outline-dark" @click="goDetail(deposit)">상세 보기</button>
            </td>
          </tr>
        </template>
      </tbody>
    </table>
</template>

<script setup>
import { productStore } from '@/stores/productStore'
import { onMounted } from 'vue'
import { useRouter } from 'vue-router'

const store = productStore()
const router = useRouter()

onMounted(() => {
  store.updateDeposit()
})

const goDetail = function (deposit) {
  console.log(deposit.fin_prdt_cd)
  router.push({name: 'productDetail', params: {type: 'deposits', pk: deposit.fin_prdt_cd}})
}

</script>

<style scoped>

</style>