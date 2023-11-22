<template>
  <li>
    <p>제목 : {{ article.title }}</p>
  </li>
  <button @click="goArticle">글로 가기</button>
</template>

<script setup>
import { useRouter } from 'vue-router'

const props = defineProps({
  'article': Object
})

const router = useRouter()

const goArticle = function() {
  router.push({ name: 'boardsDetail', params: {pk: props.article.id} })
}

</script>

<style scoped>

</style>