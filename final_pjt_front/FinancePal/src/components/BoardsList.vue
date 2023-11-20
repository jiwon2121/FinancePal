<template>
  <div>
    <h1>{{type}}</h1>
    <template v-for="board in store.boards">
      <div @click="goDetail(board.id)">
        {{ board.id }}
        {{ board.title }}
        <br>
        글쓴이 : {{ board.user.nickname }}
        <hr>
      </div>
    </template>
  </div>
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
  console.log(1111111)
}

</script>

<style scoped>

</style>