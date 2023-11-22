import { defineStore } from "pinia"
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'
import axios from 'axios'

export const profileStore = defineStore('profile', () => {
  const profile = ref(null)
  const recommend = ref(null)

  const getProfile = function(username) {
    axios({
      method: 'get',
      url: `http://127.0.0.1:8000/profile/${username}/`
    })
      .then(res => {
        profile.value = res.data
      })
      .catch(err => {
        console.log(err)
      })

    axios({
      method: 'get',
      url: `http://127.0.0.1:8000/profile/recommend_by_profile/${username}/`
    })
      .then(res => {
        recommend.value = res.data
        console.log(recommend.value)
      })
      .catch(err => {
        console.log(err)
      })
  }

  return { profile, recommend, getProfile }
})