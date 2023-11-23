<template>
  <div v-if="product">
    <button class="btn btn-secondary mb-3" @click="router.back()">뒤로 가기</button>
    <div class="product-banner border rounded mt-3 mb-5">
      <div class="p-4 header d-flex justify-content-around align-items-center">
        <div class="d-flex">
          <h1 class="me-3">🔎</h1>
          <div class="d-flex flex-column justify-content-center">
            <h1 class="product-name">{{ product.fin_prdt_nm }}</h1>
            <span>{{ product.kor_co_nm }}</span>
          </div>
        </div>
        <template v-if="store.isLogin">
          <button class='btn btn-danger' v-if="isJoin" @click="cancel">해지하기</button>
          <button class='btn btn-success' v-else @click="join">가입하기</button>
        </template>
      </div>
    </div>
    <template v-if="product">
      <div class="row">
        <div class="col-2">
          <p class="text-end"><strong>가입 방법</strong></p>
        </div>
        <div class="col-10">
          {{ product.join_way }}
        </div>
        <hr>
        <div class="col-2">
          <p class="text-end"><strong>우대 조건</strong></p>
        </div>
        <div class="col-10">
          {{ product.spcl_cnd }}
        </div>
        <hr>
        <div class="col-2">
          <p class="text-end"><strong>가입 제한</strong></p>
        </div>
        <div class="col-10">
          {{ convert(product.join_deny) }}
        </div>
        <hr>
        <div class="col-2">
          <p class="text-end"><strong>가입 대상</strong></p>
        </div>
        <div class="col-10">
          {{ product.join_member }}
        </div>
        <hr>
        <div class="col-2">
          <p class="text-end"><strong>최고 한도</strong></p>
        </div>
        <div class="col-10">
          {{ product.max_limit === null ? '제한없음' : product.max_limit.toLocaleString() + '원' }}
        </div>
        <hr>
      </div>
    </template>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import axios from 'axios'
import { accountStore } from '@/stores/accountStore'

const store = accountStore()
const route = useRoute()
const router = useRouter()
const product = ref(null)
const isJoin = computed(() => {
  let flag = false
  store[route.params.type].forEach((value) => {
    if (value.fin_prdt_cd === route.params.pk) {
      flag = true
    }
  })
  return flag
})

console.log(store.savings)

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

const join = function() {
  axios({
    method: 'post',
    url: `http://127.0.0.1:8000/profile/join/${route.params.type}/${route.params.pk}/`,
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
    .then(res => {
      store.updateProfile()
    })
}

const cancel = function() {
  axios({
    method: 'post',
    url: `http://127.0.0.1:8000/profile/cancel/${route.params.type}/${route.params.pk}/`,
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
    .then(res => {
      store.updateProfile()
    })
    .catch(err => {
      console.log(err)
    })
}

</script>

<style scoped>
.product-banner {
  background-color: whitesmoke;
}
</style>