<template>
  <div>
    <h1>게시판</h1>
    <button @click="changeType('free')">자유게시판</button>
    <button @click="changeType('qna')">Q&A</button>
    <button @click="changeType('notice')">공지사항</button>
  </div>
  <BoardsFree 
  v-if="type==='free'"
  />
  <BoardsQna 
  v-else-if="type==='qna'"
  />
  <BoardsNotice 
  v-else-if="type==='notice'"
  />
</template>

<script setup>
import { ref } from 'vue'
import BoardsFree from '@/components/BoardsFree.vue'
import BoardsQna from '@/components/BoardsQna.vue'
import BoardsNotice from '@/components/BoardsNotice.vue'

const type = ref('free')

const changeType = function(tp) {
  type.value = tp
}

</script>

<style scoped>

</style>