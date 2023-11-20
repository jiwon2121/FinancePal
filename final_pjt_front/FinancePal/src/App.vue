<template>
  <div>
    <nav>
      <RouterLink :to="{ name: 'main'}">메인</RouterLink>
      <span> | </span>
      <RouterLink :to="{ name: 'product'}">상품비교</RouterLink>
      <span> | </span>
      <RouterLink :to="{ name: 'exchange'}">환율</RouterLink>
      <span> | </span>
      <RouterLink :to="{ name: 'map'}">주위 은행</RouterLink>
      <span> | </span>
      <RouterLink :to="{ name: 'boards'}">게시판</RouterLink>
      <span> | </span>
      <template v-if="accStore.isLogin">
        <RouterLink :to="{ name: 'profile', params: { username: accStore.userName }}">프로필</RouterLink>
        <span> | </span>
        <button @click="accStore.logOut">로그아웃</button>
        <span> | </span>
      </template>
      <template v-else>
        <!-- <RouterLink :to="{ name: 'login'}">로그인</RouterLink> -->
        <button @click="goLogin">로그인</button>
        <span> | </span>
        <RouterLink :to="{ name: 'signup'}">회원가입</RouterLink>
        <span> | </span>
      </template>
    </nav>
    <RouterView />
  </div>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
import { accountStore } from '@/stores/accountStore'
import { useRouter } from 'vue-router'

const accStore = accountStore()
const router = useRouter()

const goLogin = function () {
  router.push({name: 'login'})
}
</script>

<style scoped>

</style>