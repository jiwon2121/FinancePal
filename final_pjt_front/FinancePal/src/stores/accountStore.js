import { defineStore } from "pinia"
import { ref, computed } from 'vue'

export const accountStore = defineStore('account', () => {
  const user = ref({
    username: 'USER',
  })

  return { user }
})