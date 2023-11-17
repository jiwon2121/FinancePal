import { defineStore } from "pinia"
import { ref, computed } from 'vue'

export const accountStore = defineStore('account', () => {
  // const API_URL = 'http://127.0.0.1:8000'
  const user = ref({
    username: 'USER',
  })
  const token = ref(null)
  const isLogin = computed(() => {
    if (token.value === null) {
      return false
    } else {
      return true
    }
  })

  const logIn = function(payload) {
    const {username, password} = payload
    
    axios({
      method: 'post',
      url: `${API_URL}/accounts/login/`,
      data: {
        username, password
      }
    })
    .then(res => {
      console.log(res.data)
      token.value = res.data.key
    })
    .catch(err => {
      console.log(err)
    })
  }

  const logOut = function() {
    token.value = null
  }

  return { user, token, isLogin, logIn, logOut }
})