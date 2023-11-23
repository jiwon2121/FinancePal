<template>
  <div class="d-flex flex-column align-items-center justify-content-center">
    <h1 class="my-3 mb-3">💵 실시간 환율 정보</h1>
    <div class="d-flex flex-column mt-3">
      <div class="input-group mb-3">
        <span class="input-group-text d-flex justify-content-center">대한민국 원화</span>
        <div>
          <input type="number" class="form-control text-end" v-model="korInput" @input="calOther" placeholder="금액을 입력하세요.">
          <span class="form-control text-end text-secondary overflow-hidden">{{ korInputComputed }}</span>
        </div>
      </div>
      <div class="input-group flex-nowrap">
        <select class="input-group-text" name="other" id="other" v-model="country" @change="calOther">
          <template v-for="exchange in store.exchangeList">
            <option :value="exchange.cur_nm">{{ exchange.cur_nm }}</option>
          </template>
        </select>
        <div>
          <input class="form-control text-end" type="number" v-model="otherInput" @input="calKor" placeholder="금액을 입력하세요.">
          <span class="form-control text-end text-secondary overflow-hidden">{{ otherInputComputed }}</span>
        </div>
      </div>
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
const korInput = ref(null)
const korInputComputed = computed(() => {
  return korInput.value ? korInput.value.toLocaleString() + ' 원' : '0 원'
})
const otherInputComputed = computed(() => {
  if (country.value.split(" ").length > 1) {
    return otherInput.value ? otherInput.value.toLocaleString() + " " + country.value.split(" ")[1] : '0 ' + country.value.split(" ")[1]
  } else {
    return otherInput.value ? otherInput.value.toLocaleString() + " " + country.value : '0 ' + country.value
  }
})
const otherInput = ref(null)

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
.input-group-text {
  width: 200px;
}
.form-control {
  width: 300px;
}
input[type="number"]::-webkit-outer-spin-button,
input[type="number"]::-webkit-inner-spin-button {
    -webkit-appearance: none;
    margin: 0;
}
</style>