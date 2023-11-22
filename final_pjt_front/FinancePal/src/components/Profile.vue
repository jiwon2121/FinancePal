<template>
  <div v-if="store.profile">
    <h1>{{ store.profile.nickname }}님의 프로필</h1>
    <p>생년월일 : {{ store.profile.birth_date }}</p>
    <p>이메일 : {{ store.profile.email }}</p>
    <p>성: {{ store.profile.last_name }}</p>
    <p>이름: {{ store.profile.first_name }}</p>
    <p>내가 쓴 글</p>
    <ul>
      <ProfileArticle 
        v-for="article in store.profile.article_set"
        :article="article"
      />
    </ul>
    <p>내가 쓴 댓글</p>
    <ul>
      <ProfileComment 
        v-for="comment in store.profile.comment_set"
        :comment="comment"
      />
    </ul>
  </div>
</template>

<script setup>
import { profileStore } from '@/stores/profileStore'
import ProfileArticle from '@/components/ProfileArticle.vue'
import ProfileComment from '@/components/ProfileComment.vue'

const store = profileStore()

</script>

<style scoped>

</style>