import { defineStore } from "pinia"
import { ref, computed } from 'vue'
import axios from 'axios'

export const productStore = defineStore('product', () => {
  const API_URL = 'http://127.0.0.1:8000'
  
  const deposits = ref(null)
  const savings = ref(null)

  const findDepositRate = function(opt, trm) {
    const obj = opt.find((element) => element.save_trm === trm)
    if (obj === undefined) {
      return '-'
    } else {
      return obj.intr_rate
    }
  }

  const findSavingRate = function(opt, trm, type) {
    const obj = opt.find((element) => element.save_trm === trm && element.rsrv_type === type)
    if (obj === undefined) {
      return '-'
    } else {
      return obj.intr_rate
    }
  }

  axios({
    url: `${API_URL}/products/deposits/`,
    method: 'get'
  })
    .then(res => {
      console.log(res.data)
      deposits.value = res.data
    })
    .catch(err => {
      console.log(err)
    })

  axios({
    url: `${API_URL}/products/savings/`,
    method: 'get'
  })
    .then(res => {
      savings.value = res.data
    })
    .catch(err => {
      console.log(err)
    })

  return { deposits, savings, findDepositRate, findSavingRate }
})