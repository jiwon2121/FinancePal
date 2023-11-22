<template>
  <div class="d-flex flex-column align-items-center justify-content-center">
    <h1 class="my-3 mb-3">💵 실시간 환율 정보</h1>
    <div class="d-flex flex-column mt-3">
      <div class="input-group mb-3">
        <span class="input-group-text">대한민국 원화</span>
        <input type="number" class="form-control" v-model="korInput" @input="calOther">
      </div>
      <div class="input-group flex-nowrap">
        <select class="input-group-text" name="other" id="other" v-model="country" @change="calOther">
          <template v-for="exchange in store.exchangeList">
            <option :value="exchange.cur_nm">{{ exchange.cur_nm }}</option>
          </template>
        </select>
        <input class="form-control" type="number" v-model="otherInput" @input="calKor">
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
.input-group-text {
  width: 150px;
}
</style>