<template>
  <div class="header">
    <h1>게시판</h1>
    <button @click="changeType('free')">자유게시판</button>
    <button @click="changeType('qna')">Q&A</button>
    <button @click="changeType('notice')">공지사항</button>
    <button @click="create">글쓰기</button>
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