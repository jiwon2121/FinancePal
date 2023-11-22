<template>
  <li>
    <p>제목 : {{ comment.article.title }}</p>
    <p>댓글 : {{ comment.content }}</p>
  </li>
  <button @click="goArticle">글로 가기</button>
</template>

<script setup>
import { useRouter } from 'vue-router'

const props = defineProps({
  'comment': Object
})

const router = useRouter()

const goArticle = function() {
  router.push({ name: 'boardsDetail', params: {pk: props.comment.article.id} })
}

</script>

<style scoped>

</style>