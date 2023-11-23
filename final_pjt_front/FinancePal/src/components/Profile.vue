<template>
  <div v-if="store.profile" class="mt-4 mt-3 mb-5">
    <h1 class="text-center">{{ store.profile.nickname }}님의 프로필</h1>
    <hr>
    <div class="row">
      <div class="col-2">
        <p>이름: {{ store.profile.last_name }}{{ store.profile.first_name }}</p>
        <p>생일 : {{ store.profile.birth_date }}</p>
        <p>이메일 : {{ store.profile.email }}</p>
      </div>
      <div class="col-5">
        <p>내가 쓴 글</p>
        <ul>
          <ProfileArticle 
            v-for="article in store.profile.article_set"
            :article="article"
          />
        </ul>
      </div>
      <div class="col-5">
        <p>내가 쓴 댓글</p>
        <ul>
          <ProfileComment 
            v-for="comment in store.profile.comment_set"
            :comment="comment"
          />
        </ul>
      </div>
    </div>
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