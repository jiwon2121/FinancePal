<template>
  <div class="main-body">
    <nav class="navbar navbar-dark navbar-expand-lg fixed-top">
      <div class="container-fluid">
        <RouterLink class="navbar-brand" :to="{ name: 'main'}">FinancePal</RouterLink>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="nav nav-underline navbar-nav me-auto mb-2 mb-lg-0 ms-5">
            <li class="nav-item">
              <RouterLink class="nav-link hamburger-list" :to="{ name: 'product'}">상품비교</RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink class="nav-link hamburger-list" :to="{ name: 'exchange'}">환율</RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink class="nav-link hamburger-list" :to="{ name: 'map'}">주위 은행</RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink class="nav-link hamburger-list" :to="{ name: 'boards'}">게시판</RouterLink>
            </li>
          </ul>
          <ul class="mb-lg-0 d-flex justify-content-end">
            <template v-if="accStore.isLogin">
              <button class="btn btn-sm me-3 auth-link">
                <RouterLink class="nav-link" :to="{ name: 'profile', params: { username: accStore.userName }}">프로필</RouterLink>
              </button>
              <button type="button" class="auth-log me-3 btn btn-sm" @click="accStore.logOut">로그아웃</button>
            </template>
            <template v-else>
              <button class="btn btn-outline-info me-3 auth-link">
                <RouterLink class="nav-link" :to="{ name: 'signup'}">회원가입</RouterLink>
              </button>
              <button type="button" class="auth-log me-3 btn btn-outline-info" @click="goLogin">로그인</button>
            </template>
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
.main-body {
  width: 100%;
}
.navbar {
  background-color: #146C94;
}
.navbar-brand {
  color: #AFD3E2;
  margin-left: 5%;
}
.hamburger-list {
  color: #F6F1F1;
}
.router-view {
  margin-top: 75px;
}
.auth-log {
  background-color: #AFD3E2;
  border-color: #19A7CE;
  color: #146C94;
}
.auth-link {
  background-color: #F6F1F1;
  border-color: #19A7CE;
  color: #146C94;
}
.auth-div {
  position: relative;
  background-color: #146C94;
}
</style>