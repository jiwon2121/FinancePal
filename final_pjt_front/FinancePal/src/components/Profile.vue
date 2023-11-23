<template>
  <div v-if="store.profile" class="mt-4 mt-3 mb-5">
    <h1 class="text-center">{{ store.profile.nickname }}님의 활동내역</h1>
    <hr>
    <div class="row">
      <div class="col-3">
        <ul class="list-group">
          <li class="list-group-item p-0">
            <div class="row">
              <div class="col-3 ms-2">
                <p class="text-center mt-3">이름</p>
              </div>
              <div class="col-8">
                <p class="mt-3">{{ store.profile.last_name }}{{ store.profile.first_name }}</p>
              </div>
            </div>
          </li>
          <li class="list-group-item p-0">
            <div class="row">
              <div class="col-3 ms-2">
                <p class="text-center mt-3">생일</p>
              </div>
              <div class="col-8">
                <p class="mt-3">
                  {{ store.profile.birth_date.slice(5, 7) + "/" + store.profile.birth_date.slice(8, 10)}}
                </p>
              </div>
            </div>
          </li>
          <li class="list-group-item p-0">
            <div class="row">
              <div class="col-3 ms-2">
                <p class="text-center mt-3">메일</p>
              </div>
              <div class="col-8">
                <p class="mt-3 overflow-x-hidden">{{ store.profile.email }}</p>
              </div>
            </div>
          </li>
        </ul>
      </div>
      <div class="col-9 row">
        <div class="col-6">
          <table class="table table-striped">
            <thead>
              <tr class="text-center">
                <th class="col-8">작성글</th>
                <th class="col-4">작성일</th>
              </tr>
            </thead>
            <tbody class="table-group-divider">
            <ProfileArticle 
              v-for="article in store.profile.article_set"
              :article="article"
            />
            </tbody>
          </table>
        </div>
        <div class="col-6">
          <table class="table table-striped">
            <thead>
              <tr class="text-center">
                <th class="col-8">댓글</th>
                <th class="col-4">날짜</th>
              </tr>
            </thead>
            <tbody class="table-group-divider">
              <ProfileComment 
                v-for="comment in store.profile.comment_set"
                :comment="comment"
              />
            </tbody>
          </table>
        </div>

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