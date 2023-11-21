<template>
  <div v-if="board">
    <h1>게시판 세부</h1>
    <h3>{{ board.title }}</h3>
    <button
    v-if="store.userName===board.user.username"
    @click="deleteArticle"
    >
    삭제
    </button>
    <hr>
    <p>글쓴이 : {{ board.user.nickname }}</p>
    <p>댓글 수 : {{ board.comment_set.length }}</p>
    <hr>
    <p>{{ board.content }}</p>
    <hr>
    <p>댓글 작성</p>
    <form v-if="store.isLogin" @submit.prevent="writeComment">
      <input type="text" ref="comment">
      <button>작성</button>
    </form>
    <hr>
    <h3>댓글</h3>
    <template v-for="comment in board.comment_set">
      <p>{{ comment.content }}</p>
      <p>댓글작성자: {{ comment.user.nickname }}</p>
      <!-- <button 
      v-if="store.userName===comment.user.username"
      @click=""
      >
      삭제</button>
      <hr> -->
    </template>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { accountStore } from '@/stores/accountStore'
import axios from 'axios'

const store = accountStore()
const board = ref(null)
const route = useRoute()
const router = useRouter()

const comment = ref(null)

const writeComment = function() {
  axios({
    method: 'post',
    url: `http://127.0.0.1:8000/articles/${route.params.pk}/`,
    data: {
      username: store.userName,
      content: comment.value.value
    }
  })
    .then(res => {
      updateComment()
    })
    .catch(err => {
      console.log(err)
    })
}

//댓글 삭제 : 추후 수정
// const deleteComment = function() {
//   axios({
//     method: 'delete',
//     url: `http://127.0.0.1:8000/articles/${route.params.pk}/`,

//   })
// }

const deleteArticle = function() {
  axios({
    method: 'delete',
    url: `http://127.0.0.1:8000/articles/${route.params.pk}/`,
    // data:{ username: user.userName }
  })
    .then(() => {
      router.push({name: 'boards'})
    })
}

const updateComment = function() {
  axios({
    method: 'get',
    url: `http://127.0.0.1:8000/articles/${route.params.pk}/`
  })
    .then(res => {
      board.value = res.data
      console.log(board.value)
    })
    .catch(err => {
      console.log(err)
    })
}

onMounted(updateComment)

</script>

<style scoped>

</style>