<template>
  <tr class="p-0">
      <td>
        <a href=""
          class="link-body-emphasis link-offset-2 link-underline-opacity-25 link-underline-opacity-75-hover"
          @click="goArticle">{{ comment.content }}
        </a>
      </td>
      <td>
        <span>
          {{ comment.created_at.slice(0, 10) }}
        </span>
      </td>
  </tr>
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