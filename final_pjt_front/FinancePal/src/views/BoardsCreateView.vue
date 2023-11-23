<template>
  <div>
    <button class="btn btn-secondary mb-3" @click="router.back()">뒤로 가기</button>
    <h1>✏ 글쓰기</h1>
    <br>
    <div class="form-group">
      <form @submit.prevent="create">
        <div class="d-flex justify-content-between">
          <div class="input-group board-type-select">
            <span class="input-group-text" id="board-type">탭</span>
            <select class="form-select" name="board-type" id="board-type" v-model="boardType">
              <option class="text-center" :value="null" disabled>--게시판 탭--</option>
              <option class="text-center" value="free">자유</option>
              <option class="text-center" value="qna">Q&A</option>
              <option class="text-center" value="notice" v-if="store.isStaff || store.isSuper">공지사항</option>
            </select>
          </div>
          <button class="create-btn btn btn-success">글쓰기</button>
        </div>
        <p v-if="typeAlert" class="text-danger my-0">!게시판 종류를 선택하세요!</p>
        <br>
        <div class="input-group">
          <span class="input-group-text" id="title">제목</span>
          <input type="text" class="form-control" placeholder="제목을 입력하세요." ref="title" aria-describedby="title">
        </div>
        <p v-if="titleAlert" class="text-danger my-0">!제목을 작성하세요!</p>
        <br>
        <div class="input-group">
          <span class="input-group-text" id="content">내용</span>
          <textarea class="form-control" name="content" id="content" cols="30" rows="10" ref="content" placeholder="내용을 입력하세요."></textarea>
        </div>
        <p v-if="contentAlert" class="text-danger my-0">!내용을 작성하세요!</p>
      </form>
    </div>
  </div>
</template>

<script setup>
import { accountStore } from '@/stores/accountStore'
import { useRouter, onBeforeRouteLeave } from 'vue-router'
import { ref } from 'vue'
import axios from 'axios'

const store = accountStore()
const router = useRouter()
const boardType = ref(null)
const title = ref(null)
const content = ref(null)
const isSave = ref(false)
const typeAlert = ref(false)
const titleAlert = ref(false)
const contentAlert = ref(false)

onBeforeRouteLeave ((to, from, next) => {
  if (isSave.value === false) {
    const result = window.confirm('저장되지 않았습니다. 그래도 떠나시겠습니까?')
    if (result) {
      next()
    }
  } else {
    next()
  }
})

const create = function() {

  const data = {
    username: store.userName,
    board_type: boardType.value,
    title: title.value.value,
    content: content.value.value
  }
  console.log(data)
  axios({
    method: 'post',
    url: `http://127.0.0.1:8000/articles/${boardType.value}/`,
    data,
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
    .then(res => {
      isSave.value = true
      router.replace({name: 'boards'})
    })
    .catch(err => {
      if (!data.board_type) {
        typeAlert.value = true
      } else {
        typeAlert.value = false
      }
      if (!data.title) {
        titleAlert.value = true
      } else {
        titleAlert.value = false
      }
      if (!data.content) {
        contentAlert.value = true
      } else {
        contentAlert.value = false
      }
    })
}
</script>

<style scoped>
.form-select {
  width: 40%;
}

.board-type-select {
  width: 60%;
}

#content {
  height: 400px;
}
</style>