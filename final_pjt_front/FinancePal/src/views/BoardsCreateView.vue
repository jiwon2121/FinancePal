<template>
  <div>
    <h1>글쓰기</h1>
    <form @submit.prevent="create">
      <select name="board-type" id="board-type" v-model="boardType">
        <option value="" disabled>--게시판 종류--</option>
        <option value="free">자유게시판</option>
        <option value="qna">Q&A</option>
        <option value="notice" v-if="store.isStaff || store.isSuper">공지사항</option>
      </select>
      <br>
      <span> 제목 : </span>
      <input type="text" v-model="title">
      <br>
      <span> 내용 : </span>
      <textarea name="content" id="content" cols="30" rows="10" v-model="content"></textarea>
      <button>글쓰기</button>
    </form>
  </div>
</template>

<script setup>
import { accountStore } from '@/stores/accountStore'
import { useRouter } from 'vue-router'
import { ref } from 'vue'
import axios from 'axios'

const store = accountStore()
const router = useRouter()
const boardType = ref('free')
const title = ref('')
const content = ref('')

const create = function() {
  const data = {
    user_id: store.userPk,
    board_type: boardType.value,
    title: title.value,
    content: content.value
  }
  console.log(data)
  axios({
    method: 'post',
    url: `http://127.0.0.1:8000/articles/${boardType.value}/`,
    data
  })
    .then(res => {
      router.replace({name: 'boards', params: {page: 1}})
    })
    .catch(err => {
      console.log(err)
    })
}
</script>

<style scoped>

</style>