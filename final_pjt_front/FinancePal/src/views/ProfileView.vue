<template>
  <div>
    <!-- <nav v-if="route.params.username === acc.userName"> -->
    <nav>
      <button @click="changePage(1)">프로필</button>
      <button @click="changePage(2)">포트폴리오</button>
      <button @click="changePage(3)">상품추천</button>
    </nav>
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
import { useRoute, onBeforeRouteUpdate } from 'vue-router'
import { profileStore } from '@/stores/profileStore'
import { accountStore } from '@/stores/accountStore'
import Portfolio from '@/components/Portfolio.vue'
import Profile from '@/components/Profile.vue'
import Recommend from '@/components/Recommend.vue'

const page = ref(1)
const store = profileStore()
const acc = accountStore()
const route = useRoute()

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