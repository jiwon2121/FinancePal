<template>
  <div>
    <div class="d-flex justify-content-between">
      <button class="mx-1 btn btn-secondary" @click="router.back()">뒤로 가기</button>
      <div>
        <button type="button" class="mx-1 btn btn-outline-dark" :class="{active:page===1}" @click="changePage(1)">활동내역</button>
        <button type="button" class="mx-1 btn btn-outline-dark" :class="{active:page===2}" v-if="route.params.username===accStore.userName" @click="changePage(2)">포트폴리오</button>
        <button type="button" class="mx-1 btn btn-outline-dark" :class="{active:page===3}" v-if="route.params.username===accStore.userName" @click="changePage(3)">상품 추천</button>
      </div>
    </div>
    <Profile 
      v-if="page===1"
    />
    <Portfolio 
      v-if="page===2"
    />
    <Recommend 
      v-if="page===3"
    />
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute, useRouter, onBeforeRouteUpdate } from 'vue-router'
import { profileStore } from '@/stores/profileStore'
import { accountStore } from '@/stores/accountStore'
import Portfolio from '@/components/Portfolio.vue'
import Profile from '@/components/Profile.vue'
import Recommend from '@/components/Recommend.vue'

const page = ref(1)
const store = profileStore()
const route = useRoute()
const router = useRouter()
const accStore = accountStore()

const changePage = function(num) {
  page.value = num
}

onMounted(() => {
  store.getProfile(route.params.username)
})

onBeforeRouteUpdate((to) => {
  store.getProfile(to.params.username)
  page.value = 1
})

</script>

<style scoped>

</style>