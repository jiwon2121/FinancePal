<template>
  <table class="table table-striped">
    <thead>
      <tr class="text-center">
        <th class="col-2">글쓴이</th>
        <th class="col-6">제목</th>
        <th class="col-3">날짜</th>
      </tr>
    </thead>
    <tbody class="table-group-divider">
      <div class="spinner-border" role="status" v-if="store.isLoad">
        <span class="visually-hidden">Loading...</span>
      </div>
      <template v-for="board in store.boards" v-else>
        <tr>
          <td class="text-center">{{ board.user.nickname }}</td>
          <td><a href="" class="link-body-emphasis link-offset-2 link-underline-opacity-25 link-underline-opacity-75-hover" @click="goDetail(board.id)">{{ board.title }}</a></td>
          <td class="text-center">{{ board.created_at.slice(0, 10) }}</td>
        </tr>
    </template>
  </tbody>
  </table>
</template>

<script setup>
import { onMounted, watch } from 'vue'
import { boardsStore } from '@/stores/boardsStore'
import { useRouter } from 'vue-router'

const props = defineProps({
  type: String
})

const router = useRouter()
const store = boardsStore()
onMounted(() => {
  store.updateBoards(props.type)
})

const propsWatch = watch(props, (newValue) => {
  store.updateBoards(props.type)
})

const goDetail = function(pk) {
  router.push({name: "boardsDetail", params: {pk: pk}})
}

</script>

<style scoped>
.table {
  width: 100%;
}
.spinner-border {
  position: absolute;
  top: 50%;
  left: 50%;
}
</style>