<template>
  <div class="d-flex flex-column align-items-center justify-content-center">
    <h1 class="my-3 mb-3">💵 실시간 환율 정보</h1>
    <div class="d-flex flex-column mt-3">
      <div class="input-group mb-3">
        <span class="input-group-text d-flex justify-content-center flex-column">
          <p class="mt-2">대한민국 원화</p>
          <div>
            <button class="btn btn-sm btn-outline-success" @click="increase(1)">+1만</button>
            <button class="btn btn-sm btn-outline-success mx-1" @click="increase(10)">+10만</button>
            <button class="btn btn-sm btn-outline-success" @click="increase(100)">+100만</button>
          </div>
        </span>
        <div class="d-flex flex-column">
          <input type="number" class="form-control text-end kor-input" v-model="korInput" @input="calOther" placeholder="금액을 입력하세요.">
          <span class="form-control text-end text-secondary overflow-x-hidden">{{ korInputComputed }}</span>
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
          <span class="form-control text-end text-secondary overflow-x-hidden">{{ otherInputComputed }}</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { exchangeStore } from '@/stores/exchangeStore'
import { onMounted } from 'vue'

const korInput = ref(null)
const otherInput = ref(null)
const store = exchangeStore()
const country = ref('미국 달러')
const exchangeRate = computed(() => {
  const idx = store.exchangeList.findIndex((ele) => ele.cur_nm === country.value)
  const ex = store.exchangeList[idx].deal_bas_r.replace(',', '')
  return parseFloat(ex)
})
const korInputComputed = computed(() => {
  return korInput.value ? korInput.value.toLocaleString() + ' 원' : '0 원'
})
const otherInputComputed = computed(() => {
  if (country.value.split(" ").length > 1) {
    return otherInput.value ? otherInput.value.toString()
  .replace(/\B(?<!\.\d*)(?=(\d{3})+(?!\d))/g, ",") + " " + country.value.split(" ")[1] : '0 ' + country.value.split(" ")[1]
  } else {
    return otherInput.value ? otherInput.value.toString()
  .replace(/\B(?<!\.\d*)(?=(\d{3})+(?!\d))/g, ",") + " " + country.value : '0 ' + country.value
  }
})

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

const increase = function(number) {
  korInput.value += number * 10000
  calOther()
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
.kor-input {
  height: 60px;
}
</style>