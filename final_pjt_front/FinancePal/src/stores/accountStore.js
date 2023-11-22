import { defineStore } from "pinia"
import { ref, computed, watch } from 'vue'
import { useRouter } from 'vue-router'
import axios from 'axios'

export const accountStore = defineStore('account', () => {
  const API_URL = 'http://127.0.0.1:8000'
  const router = useRouter()
  
  const userName = ref(null)
  const token = ref(null)
  const isSuper = ref(null)
  const isStaff = ref(null)
  const address = ref(null)
  const city = ref('')
  const area = ref('')

  const addressWatch = watch(address, (newValue) => {
    const splited = newValue.split(' ')
    city.value = splited[0]
    area.value = splited[1]
  })

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
      },
    })
      .then(res => {
        const back = history.state.back
        token.value = res.data.key
        userName.value = username
        router.replace(`${back}`)
      })
      .then(res => {
        axios({
          method: 'post',
          url: `${API_URL}/profile/permission/${username}/`,
          headers: {
            Authorization: `Token ${token.value}`
          }
        })
          .then(res => {
            isStaff.value = res.data.is_staff
            isSuper.value = res.data.is_super
          })
      })
      .catch(err => {
        console.log(err)
      })
      

    axios({
      method: 'get',
      url: `${API_URL}/profile/${username}`
    })
      .then(res => {
        console.log(res.data)
        address.value = res.data.address
      })
  }

  const logOut = function() {
    localStorage.removeItem('account')
    location.reload()
  }

  return { userName, token, isStaff, isSuper, isLogin, city, area, logIn, logOut }
}, { persist: true })