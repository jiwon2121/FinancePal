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
  const ex = store.exchangeList[idx].deal_bas_r.replace(',', '')
  return parseFloat(ex)
})
const korInput = ref(0)
const otherInput = ref(0)

const calOther = function() {
  const temp = korInput.value / exchangeRate.value
  if (temp >= 1) {
    otherInput.value = temp.toFixed(2)
  } else {
    const expo = temp.toExponential(1)
    otherInput.value = parseFloat(expo)
  }
}
const calKor = function() {
  const temp = otherInput.value * exchangeRate.value
  if (temp >= 1) {
    korInput.value = temp.toFixed(2)
  } else {
    const expo = temp.toExponential(1)
    korInput.value = parseFloat(expo)
  }
}


onMounted(() => {
  store.updateExchange()
})

</script>

<style scoped>

</style>