<template>
  <div>
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
        <template v-for="saving in store.savings">
          <tr>
            <td>{{ saving.kor_co_nm }}</td>
            <td>{{ saving.fin_prdt_nm }}</td>
            <td>{{ store.findSavingRate(saving.savingoption_set, '6', 'F')}}</td>
            <td>{{ store.findSavingRate(saving.savingoption_set, '12', 'F') }}</td>
            <td>{{ store.findSavingRate(saving.savingoption_set, '24', 'F') }}</td>
            <td>{{ store.findSavingRate(saving.savingoption_set, '36', 'F') }}</td>
            <td>
              <button type="button" class="btn btn-outline-dark" @click="goDetail(saving)">상세 보기</button>
            </td>
          </tr>
        </template>
      </tbody>
    </table>
  </div>
</template>

<script setup>
import { productStore } from '@/stores/productStore'
import { onMounted } from 'vue'
import { useRouter } from 'vue-router'

const store = productStore()
const router = useRouter()

onMounted(() => {
  store.updateSaving()
})

const goDetail = function (saving) {
  console.log(saving.fin_prdt_cd)
  router.push({name: 'productDetail', params: {type:'savings', pk: saving.fin_prdt_cd}})
}

</script>

<style scoped>

</style>