import { defineStore } from "pinia"
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'
import axios from 'axios'

export const boardsStore = defineStore('boards', () => {
  const boards = ref(null)
  const updateBoards = function(type) {
    axios({
      method:'get',
      url: `http://127.0.0.1:8000/articles/${type}/`
    })
      .then(res => {
        boards.value = res.data
      })
  }

  return { boards, updateBoards }
})