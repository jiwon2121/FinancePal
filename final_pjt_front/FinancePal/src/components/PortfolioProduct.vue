<template>
  <li>
    <span>{{ product.fin_prdt_nm }}</span>
    <button @click="goProduct">상품 페이지</button>
  </li>
</template>

<script setup>
import { useRouter } from 'vue-router'

const router = useRouter()
// const props = defineProps({
//   product: Object
//   type: String
// })
const props = defineProps(['product', 'type'])

const goProduct = function() {
  router.push({name: 'productDetail', params: {type: props.type, pk: props.product.fin_prdt_cd}})
}
</script>

<style scoped>

</style>