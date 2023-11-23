<template>
  <div v-if="board">
    <button class="btn btn-secondary mb-3" @click="router.back()">뒤로 가기</button>
    <template v-if="isEdit">
      <h1>📝 글 수정하기</h1>
      <br>
      <div class="form-group">
        <form @submit.prevent>
          <div class="d-flex justify-content-between">
            <div class="input-group board-type-select">
              <span class="input-group-text" id="board-type">탭</span>
              <select class="form-select" name="board-type" id="board-type" v-model="boardType">
                <option class="text-center" value="free">자유</option>
                <option class="text-center" value="qna">Q&A</option>
                <option class="text-center" value="notice" v-if="store.isStaff || store.isSuper">공지사항</option>
              </select>
            </div>
            <div class="d-flex">
              <button class="btn btn-secondary me-3" @click="changeState">취소</button>
              <button class="btn btn-success" @click="editArticle">수정</button>
            </div>
          </div>
          <br>
          <div class="input-group">
            <span class="input-group-text" id="title">제목</span>
            <input class="form-control" type="text" :value="board.title" ref="titleInput" aria-describedby="title">
          </div>
          <br>
          <div class="input-group">
            <span class="input-group-text" id="content">내용</span>
            <textarea class="form-control" name="content" id="content" cols="30" rows="10" ref="contentInput">{{ board.content }}</textarea>
          </div>
        </form>
      </div>
    </template>
    
    <template v-else>
      <div class="header d-flex justify-content-between align-items-center">
        <h1 class="mt-3">{{ board.title }}</h1>
        
        <template
          v-if="store.userName===board.user.username"
        >
        <div>
          <button
            class="btn btn-success me-3"
            @click="changeState"
          >
            수정
          </button>
          <button
            class="btn btn-danger"
            @click="deleteArticle"
          >
            삭제
          </button>
        </div>
        </template>
      </div>
      <hr>
      <div class="d-flex justify-content-between">
        <a href="" class="link-body-emphasis link-offset-2 link-underline-opacity-25 link-underline-opacity-75-hover" @click="goProfile(board.user.username)">{{ board.user.nickname }}</a>
        <span>댓글 : {{ board.comment_set.length }}</span>
      </div>
      <hr>
      <p class="content">{{ board.content }}</p>
      <hr>
      <div class="comment-box">
        <h4>댓글 작성하기</h4>
        <form v-if="store.isLogin" @submit.prevent="writeComment" ref="commentForm">
          <div class="input-group comment-section">
            <textarea class="form-control" name="comment" id="comment" cols="30" rows="3" ref="comment"></textarea>
            <button class="btn btn-primary">작성</button>
          </div>
        </form>
        <form v-if="!store.isLogin" @submit.prevent="writeComment" ref="commentForm">
          <div class="input-group comment-section">
            <textarea class="form-control" name="comment" id="comment" cols="30" rows="3" ref="comment" placeholder="댓글을 작성하려면 로그인하세요." disabled="true"></textarea>
            <button class="btn btn-primary" disabled="true">작성</button>
          </div>
        </form>
      </div>
      <hr>
    </template>
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
      content: comment.value.value,
    },
    headers: {
      Authorization: `Token ${store.token}`
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
    headers: {
      Authorization: `Token ${store.token}`
    }
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
    },
    headers: {
      Authorization: `Token ${store.token}`
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

const goProfile = function(username) {
  router.push({name: "profile", params: {username: username}})
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
.content {
  height: 300px;
}
.comment-section {
  width: 70%;
}
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