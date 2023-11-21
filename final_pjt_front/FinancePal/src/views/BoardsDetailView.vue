<template>
  <div v-if="board">
    <h1>게시판 세부</h1>
    <hr>
    
    <template v-if="isEdit">
      <form @submit.prevent="editArticle">
        <select name="board-type" id="board-type" v-model="boardType">
          <option value="" disabled>--게시판 종류--</option>
          <option value="free">자유게시판</option>
          <option value="qna">Q&A</option>
          <option value="notice" v-if="store.isStaff || store.isSuper">공지사항</option>
        </select>
        <br>
        <input type="text" :value="board.title" ref="titleInput">
        <hr>
        <textarea name="content" id="content" cols="30" rows="10" ref="contentInput">{{ board.content }}</textarea>
        <button>수정</button>
      </form>
      <button @click="changeState">취소</button>
    </template>

    <template v-else>
      <h3>{{ board.title }}</h3>
      <hr>
      <p>글쓴이 : {{ board.user.nickname }}</p>
      <p>댓글 수 : {{ board.comment_set.length }}</p>
      <hr>
      <p>{{ board.content }}</p>
      <template
        v-if="store.userName===board.user.username"
      >
        <button
          @click="changeState"
        >
          수정
        </button>
        <button
          @click="deleteArticle"
        >
          삭제
        </button>
      </template>
    </template>
    <hr>
    <h3>댓글</h3>
    <form v-if="store.isLogin" @submit.prevent="writeComment" ref="commentForm">
      <input type="text" ref="comment">
      <button>작성</button>
    </form>
    <hr>
    <template v-for="comment in board.comment_set">
      <Comment 
        :comment="comment"
        @updatePage="updatePage"
      />
    </template>
  </div>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { accountStore } from '@/stores/accountStore'
import Comment from '@/components/Comment.vue'
import axios from 'axios'

const store = accountStore()
const board = ref(null)
const route = useRoute()
const router = useRouter()
const commentForm = ref(null)
const comment = ref(null)
const titleInput = ref(null)
const contentInput = ref(null)
const boardType = ref(null)
const isEdit = ref(false)

const boardWatch = watch(board, (newValue) => {
  boardType.value = newValue.board_type
})

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
      commentForm.value.reset()
      updatePage()
    })
    .catch(err => {
      console.log(err)
    })
}

const deleteArticle = function() {
  axios({
    method: 'delete',
    url: `http://127.0.0.1:8000/articles/${route.params.pk}/`,
  })
    .then(() => {
      router.push({name: 'boards'})
    })
    .catch(err => {
      console.log(err)
    })
}

const editArticle = function() {
  axios({
    method: 'put',
    url: `http://127.0.0.1:8000/articles/${route.params.pk}/`,
    data: {
      board_type: boardType.value,
      title: titleInput.value.value,
      content: contentInput.value.value
    }
  })
    .then(() => {
      updatePage()
    })
    .then(() => {
      changeState()
    })
    .catch(err => {
      console.log(err)
    })
}

const changeState = function() {
  isEdit.value = !isEdit.value
}

const updatePage = function() {
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

onMounted(updatePage)

</script>

<style scoped>

</style>