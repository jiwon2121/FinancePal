<template>
  <div>
    <template v-if="isEdit">
      <div class="input-group comment-section">
        <span class="input-group-text" id="board-type">댓글 수정</span>
        <input class="form-control" type="text" :value="comment.content" ref="commentInput">
        <button class="btn btn-secondary" @click="changeState">취소</button>
        <button class="btn btn-success" @click="editComment">수정</button>
      </div>
    </template>

    <template v-else>
      <a href="" class="link-body-emphasis link-offset-2 link-underline-opacity-25 link-underline-opacity-75-hover" @click="goProfile(comment.user.username)">{{ comment.user.nickname }}</a>
      <div class="mt-3 d-flex justify-content-between">
        <p>💬 {{ comment.content }}</p>
  
        <template
          v-if="store.userName===comment.user.username"
          @click="deleteComment()"
        >
        <div>
          <button class="me-3 btn btn-success" @click="changeState">수정</button>
          <button class="btn btn-danger" @click="deleteComment">삭제</button>
        </div>
        </template>
      </div>

    </template>
    <hr>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { accountStore } from '@/stores/accountStore'
import { useRouter } from 'vue-router'
import axios from 'axios'

const router = useRouter()
const store = accountStore()
const props = defineProps({
  comment: Object
})
const emit = defineEmits(['updatePage'])

const commentInput = ref(null)

const isEdit = ref(false)

const changeState = function() {
  isEdit.value = !isEdit.value
}
const deleteComment = function() {
  axios({
    method: 'delete',
    url: `http://127.0.0.1:8000/articles/comment/${props.comment.id}/`,
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
    .then(res => {
      emit('updatePage')
    })
    .catch(err => {
      console.log(err)
    })
}

const editComment = function() {
  axios({
    method: 'put',
    url: `http://127.0.0.1:8000/articles/comment/${props.comment.id}/`,
    data: {
      content: commentInput.value.value
    },
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
    .then(res => {
      emit('updatePage')
      changeState()
    })
    .catch(err => {
      console.log(err)
    })
}

const goProfile = function(username) {
  router.push({name: "profile", params: {username: username}})
}

</script>

<style scoped>
.comment-section {
  width: 70%;
}
</style>