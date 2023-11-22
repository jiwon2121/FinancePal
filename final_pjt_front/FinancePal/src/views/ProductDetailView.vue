<template>
  <div>
    <h1>상품 상세 보기</h1>
    <template v-if="product">
      <p>금융기관 : {{ product.kor_co_nm }}</p>
      <p>상품명 : {{ product.fin_prdt_nm }}</p>
      <p>가입 방법 : {{ product.join_way }}</p>
      <p>우대 조건 : {{ product.spcl_cnd }}</p>
      <p>가입 제한 : {{ convert(product.join_deny) }}</p>
      <p>가입 대상 : {{ product.join_member }}</p>
      <p>최고 한도 : {{ product.max_limit === null ? '제한없음' : product.max_limit }}</p>
    </template>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRoute } from 'vue-router'
import axios from 'axios'

const route = useRoute()
const product = ref(null)

axios({
  method: 'get',
  url: `http://127.0.0.1:8000/products/${route.params.type}/${route.params.pk}/`
})
  .then((res) => {
    product.value = res.data
  })
  .catch((err) => {
    console.log(err)
  })

const convert = function(type) {
  if (type === 1) {
    return '제한없음'
  } else if (type === 2) {
    return '서민전용'
  } else {
    return '일부제한'
  }
}
</script>

<style scoped>

</style>