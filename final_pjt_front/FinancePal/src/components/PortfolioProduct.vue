<template>
  <li>
    <span>{{ product }}</span>
    <button @click="goProduct">상품 페이지</button>
  </li>
</template>

<script setup>
import { useRouter } from 'vue-router'

const router = useRouter()
const props = defineProps({
  product: String,
  type: String
})

const goProduct = function() {
  router.push({name: 'productDetail', params: {type: props.type, pk: props.product}})
}
</script>

<style scoped>

</style>