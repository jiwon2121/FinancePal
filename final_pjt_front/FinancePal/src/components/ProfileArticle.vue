<template>
  <tr class="p-0">
      <td>
        <a href=""
          class="link-body-emphasis link-offset-2 link-underline-opacity-25 link-underline-opacity-75-hover"
          @click="goArticle">{{ article.title }}
        </a>
      </td>
      <td>
        <span>
          {{ article.created_at.slice(0, 10) }}
        </span>
      </td>
  </tr>
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