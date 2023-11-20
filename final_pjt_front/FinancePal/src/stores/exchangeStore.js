import { defineStore } from "pinia"
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'
import axios from 'axios'

export const exchangeStore = defineStore('exchange', () => {
  const exchangeList = ref(null)
  const updateExchange = function () {
    axios({
      method: 'get',
      url: 'http://127.0.0.1:8000/exchange_rate/all/'
    })
      .then((res) => {
        exchangeList.value = res.data
      })
  }

  return { exchangeList, updateExchange }
})