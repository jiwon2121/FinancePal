import { defineStore } from "pinia"
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'
import axios from 'axios'

const exchangeStore = defineStore('exchange', () => {
  const exchageList = ref(null)

})