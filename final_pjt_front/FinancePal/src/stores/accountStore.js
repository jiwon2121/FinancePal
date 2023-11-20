import { defineStore } from "pinia"
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'
import axios from 'axios'

export const accountStore = defineStore('account', () => {
  const API_URL = 'http://127.0.0.1:8000'
  const router = useRouter()
  
  const user = ref(null)
  const userPk = ref(null)
  const token = ref(null)
  const isSuper = ref(null)
  const isStaff = ref(null)

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
        const back = history.state.back
        token.value = res.data.key
        user.value = username
        router.replace(`${back}`)
      })
      .catch(err => {
        console.log(err)
      })

    axios({
      method: 'post',
      url: `${API_URL}/profile/permission/${username}/`
    })
      .then(res => {
        isStaff.value = res.data.is_staff
        isSuper.value = res.data.is_super
        userPk.value = res.data.pk
      })
  }

  const logOut = function() {
    localStorage.removeItem('account')
    location.reload()
  }

  return { user, token, isStaff, isSuper, userPk, isLogin, logIn, logOut }
}, { persist: true })