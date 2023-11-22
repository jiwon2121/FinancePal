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
      <template v-for="board in store.boards">
        <tr>
          <td class="text-center">
            <p @click="goProfile(board.user.username)">{{ board.user.nickname }}</p>
          </td>
          <td>
            <p @click="goDetail(board.id)">{{ board.title }}</p>
          </td>
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

const goProfile = function(username) {
  router.push({name: "profile", params: {username: username}})
}

</script>

<style scoped>
.table {
  width: 100%;
}
</style>