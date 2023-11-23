<template>
  <div>
    <hr>
    <table class="table table-striped">
      <thead>
        <tr>
          <th>기관명</th>
          <th>상품명</th>
          <th>6개월</th>
          <th>12개월</th>
          <th>24개월</th>
          <th>36개월</th>
        </tr>
      </thead>
      <tbody class="table-group-divider">
        <template v-for="saving in store.savings">
          <template
          v-if="store.findSavingRate(saving.savingoption_set, '6', 'F') !== '-' ||
          store.findSavingRate(saving.savingoption_set, '12', 'F') !== '-' ||
          store.findSavingRate(saving.savingoption_set, '24', 'F') !== '-' ||
          store.findSavingRate(saving.savingoption_set, '36', 'F') !== '-'
          ">
            <tr>
            <td>{{ saving.kor_co_nm }}</td>
            <td><a href="" class="link-body-emphasis link-offset-2 link-underline-opacity-25 link-underline-opacity-75-hover" @click="goDetail(saving)">{{ saving.fin_prdt_nm }}</a></td>
              <td>{{ store.findSavingRate(saving.savingoption_set, '6', 'F')}}</td>
              <td>{{ store.findSavingRate(saving.savingoption_set, '12', 'F') }}</td>
              <td>{{ store.findSavingRate(saving.savingoption_set, '24', 'F') }}</td>
              <td>{{ store.findSavingRate(saving.savingoption_set, '36', 'F') }}</td>
            </tr>
          </template>
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