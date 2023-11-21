<template>
  <div>
    <nav class="navbar navbar-expand-lg fixed-top">
      <div class="container-fluid">
        <RouterLink class="navbar-brand" :to="{ name: 'main'}">FinancePal</RouterLink>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="nav nav-underline navbar-nav me-auto mb-2 mb-lg-0">
            <li class="nav-item">
              <RouterLink class="nav-link" :to="{ name: 'product'}">상품비교</RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink class="nav-link" :to="{ name: 'exchange'}">환율</RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink class="nav-link" :to="{ name: 'map'}">주위 은행</RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink class="nav-link" :to="{ name: 'boards'}">게시판</RouterLink>
            </li>
            <div class="profile-auth d-flex">
              <template v-if="accStore.isLogin">
                <li class="nav-item mx-auto">
                  <RouterLink class="nav-link" :to="{ name: 'profile', params: { username: accStore.userName }}">프로필</RouterLink>
                </li>
                <button type="button" class="btn btn-outline-info" @click="accStore.logOut">로그아웃</button>
              </template>
              <template v-else>
                <button type="button" class="btn btn-outline-info" @click="goLogin">로그인</button>
                <li class="nav-item">
                  <RouterLink class="nav-link" :to="{ name: 'signup'}">회원가입</RouterLink>
                </li>
              </template>
            </div>
          </ul>
        </div>
      </div>
    </nav>
    <RouterView class="router-view"/>
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
.navbar {
  background-color: #146C94;
}
.navbar-brand {
  color: #AFD3E2;
  margin-left: 5%;
}
.nav-link {
  color: #F6F1F1;
}
.router-view {
  margin-top: 75px;
}
.profile-auth {
  position: absolute;
  margin-left: 65%;
}
</style>