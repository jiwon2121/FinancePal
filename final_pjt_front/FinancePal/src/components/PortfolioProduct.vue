<template>
  <tr class="p-0">
    <td class="text-center">
      <a href=""
        class="link-body-emphasis link-offset-2 link-underline-opacity-25 link-underline-opacity-75-hover"
        @click="goProduct">{{ product.fin_prdt_nm }}
      </a>
    </td>
  </tr>
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