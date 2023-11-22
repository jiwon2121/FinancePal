import { defineStore } from "pinia"
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'
import axios from 'axios'

export const boardsStore = defineStore('boards', () => {
  const boards = ref(null)
  const isLoad = ref(true)
  const updateBoards = function(type) {
    isLoad.value = true
    axios({
      method:'get',
      url: `http://127.0.0.1:8000/articles/${type}/`
    })
      .then(res => {
        isLoad.value = false
        boards.value = res.data
      })
      .catch(err => {
        console.log(err)
      })
  }

  return { boards, isLoad, updateBoards }
})