<template>
  <div>
    <h1>ExchangeView</h1>
    <div>
      <span>대한민국</span>
      <input type="number" v-model="korInput" @input="calOther">
    </div>
    <div>
      <select name="other" id="other" v-model="country" @change="calOther">
        <template v-for="exchange in store.exchangeList">
          <option :value="exchange.cur_nm">{{ exchange.cur_nm }}</option>
        </template>
      </select>
      <input type="number" v-model="otherInput" @input="calKor">
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { exchangeStore } from '@/stores/exchangeStore'
import { onMounted } from 'vue'

const store = exchangeStore()
const country = ref('미국 달러')
const exchangeRate = computed(() => {
  const idx = store.exchangeList.findIndex((ele) => ele.cur_nm === country.value)
  return store.exchangeList[idx].deal_bas_r
})
const korInput = ref(0)
const otherInput = ref(0)

const calOther = function() {
  otherInput.value = korInput.value / exchangeRate.value
}
const calKor = function() {
  korInput.value = otherInput.value * exchangeRate.value
}


onMounted(() => {
  store.updateExchange()
})

</script>

<style scoped>

</style>