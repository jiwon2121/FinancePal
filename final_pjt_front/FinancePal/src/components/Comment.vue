<template>
  <div>
    <template v-if="isEdit">
      <form @submit.prevent="editComment">
        <input type="text" :value="comment.content" ref="commentInput">
        <button>수정</button>
      </form>
      <button @click="changeState">취소</button>
    </template>

    <template v-else>
      <p>{{ comment.content }}</p>
      <p>댓글작성자: {{ comment.user.nickname }}</p>

      <template
        v-if="store.userName===comment.user.username"
        @click="deleteComment()"
      >
        <button @click="changeState">수정</button>
        <button @click="deleteComment">삭제</button>
      </template>

    </template>
    <hr>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { accountStore } from '@/stores/accountStore'
import axios from 'axios'

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

</script>

<style scoped>

</style>