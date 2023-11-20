<template>
  <div>
    <h1>{{type}}</h1>
    <p v-for="board in store.boards">{{ board.title }}
      <br>
      <!-- {{ board }}  -->
      글쓴이 : {{ board.user.nickname }}
      <hr>
    </p>
  </div>
</template>

<script setup>
import { onMounted, watch } from 'vue'
import { boardsStore } from '@/stores/boardsStore'

const props = defineProps({
  type: String
})
const store = boardsStore()
onMounted(() => {
  store.updateBoards(props.type)
})

const propsWatch = watch(props, (newValue) => {
  store.updateBoards(props.type)
})

</script>

<style scoped>

</style>