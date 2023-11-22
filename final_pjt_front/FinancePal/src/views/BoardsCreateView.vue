<template>
  <div>
    <button class="btn btn-secondary mb-3" @click="router.back()">뒤로 가기</button>
    <h1>글쓰기</h1>
    <br>
    <div class="form-group">
      <form @submit.prevent="create">
        <div class="d-flex justify-content-between">
          <div class="input-group board-type-select">
            <span class="input-group-text" id="board-type">종류</span>
            <select class="form-select" name="board-type" id="board-type" v-model="boardType">
              <option class="text-center" :value="null" disabled>--게시판 종류--</option>
              <option class="text-center" value="free">자유게시판</option>
              <option class="text-center" value="qna">Q&A</option>
              <option class="text-center" value="notice" v-if="store.isStaff || store.isSuper">공지사항</option>
            </select>
          </div>
          <button class="create-btn btn btn-success">글쓰기</button>
        </div>
        <br>
        <div class="input-group">
          <span class="input-group-text" id="title">제목</span>
          <input type="text" class="form-control" placeholder="제목을 입력하세요." v-model="title" aria-describedby="title">
        </div>
        <br>
        <div class="input-group">
          <span class="input-group-text" id="content">내용</span>
          <textarea class="form-control" name="content" id="content" cols="30" rows="10" v-model="content" placeholder="내용을 입력하세요."></textarea>
        </div>
      </form>
    </div>
  </div>
</template>

<script setup>
import { accountStore } from '@/stores/accountStore'
import { useRouter } from 'vue-router'
import { ref } from 'vue'
import axios from 'axios'

const store = accountStore()
const router = useRouter()
const boardType = ref(null)
const title = ref('')
const content = ref('')

const create = function() {
  const data = {
    username: store.userName,
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
      router.replace({name: 'boards'})
    })
    .catch(err => {
      if (boardType.value === null || title.value === '') {
        if (boardType.value === null && title.value === '') {
          window.alert('게시판 종류를 선택하고 제목을 입력하세요.')
        } else if (title.value.length > 0) {
          window.alert('게시판 종류를 선택하세요.')
        } else {
          window.alert('제목을 입력하세요.')
        }
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