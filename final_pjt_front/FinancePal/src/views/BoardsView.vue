<template>
  <div class="header mb-5 text-center">
    <h1 class="mx-3 mb-3" v-if="type === 'free'">✒ 자유 게시판</h1>
    <h1 class="mx-3 mb-3" v-if="type === 'qna'">❔ Q&A</h1>
    <h1 class="mx-3 mb-3" v-if="type === 'notice'">📢 공지사항</h1>
    <div class="d-flex justify-content-between">
      <div>
        <button type="button" class="mx-1 btn btn-outline-dark" :class="{active:type=='free'}" @click="changeType('free')">자유게시판</button>
        <button type="button" class="mx-1 btn btn-outline-dark" :class="{active:type=='qna'}" @click="changeType('qna')">Q&A</button>
        <button type="button" class="mx-1 btn btn-outline-dark" :class="{active:type=='notice'}" @click="changeType('notice')">공지사항</button>
      </div>
      <button type="button" class="btn btn-success" @click="create">글쓰기</button>
    </div>
  </div>
  <BoardsList 
  :type="type"
  />
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import BoardsList from '@/components/BoardsList.vue'

const type = ref('free')
const router = useRouter()

const changeType = function(tp) {
  type.value = tp
}

const create = function() {
  router.push({name: 'boardsCreate'})
}

</script>

<style scoped>
.header {
  margin-top: 100px;
}
</style>