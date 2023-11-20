import { defineStore } from "pinia"
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'
import axios from 'axios'

export const boardsStore = defineStore('boards', () => {
  const boards = ref(null)
  
})