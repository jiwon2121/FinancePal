<template>
  <div>
    <h1>회원가입</h1>
    <div class="form-group">
      <form @submit.prevent="signUp">
        <div class="input-group">
          <span class="input-group-text">아이디</span>
          <input class="form-control" type="text" id="username" v-model="username">
        </div>

        <div class="input-group">
          <span class="input-group-text">비밀번호</span>
          <input class="form-control" type="password" id="password1" v-model="password1">
        </div>
        <div class="input-group">
          <span class="input-group-text">비밀번호 확인</span>
          <input class="form-control" type="password" id="password2" v-model="password2">
        </div>
        <div class="input-group">
          <span class="input-group-text">성</span>
          <input class="form-control" type="text" id="lastname" ref="lastname">
        </div>
        <div class="input-group">
          <span class="input-group-text">이름</span>
          <input class="form-control" type="text" id="firstname" ref="firstname">
        </div>
        <div class="input-group">
          <span class="input-group-text">닉네임</span>
          <input class="form-control" type="text" id="nickname" v-model="nickname">
        </div>
        
        <div class="input-group">
          <span class="input-group-text">이메일</span>
          <input class="form-control" type="text" id="email-id" v-model="emailId">
          <span class="input-group-text"> @ </span>
          <input class="form-control" type="text" id="email-domain" v-model="emailDomain">
        </div>

        <div class="input-group">
          <span class="input-group-text">주소</span>
          <textarea class="form-control" name="address" id="address" cols="30" rows="10" v-model="address"></textarea>
        </div>

        <div class="input-group">
          <span class="input-group-text">생년월일</span>
          <input class="form-control" type="date" id="birth-date" v-model="birthDate">
        </div>
        <div class="input-group">
        <span class="input-group-text">성별</span>
          <select class="form-select" name="gender" id="gender" v-model="gender">
            <option value="1">남</option>
            <option value="0">여</option>
          </select>
        </div>
        <div class="input-group">
          <span class="input-group-text">연봉</span>
          <input class="form-control" type="number" v-model="salary">
        </div>
        <div class="input-group">
        <span class="input-group-text">통장 잔고</span>
        <input class="form-control" type="number" v-model="balance">
        </div>
        <button class="btn btn-success">회원 가입</button>
      </form>
    </div>
    </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import axios from 'axios'

const router = useRouter()

const username = ref(null)
const password1 = ref(null)
const password2 = ref(null)
const lastname = ref(null)
const firstname = ref(null)
const nickname = ref(null)
const emailId = ref(null)
const emailDomain = ref(null)
const address = ref(null)
const birthDate = ref(null)
const gender = ref(1)
const salary = ref(null)
const balance = ref(null)
// const deposit_products = ref([])
// const saving_products = ref([])

const signUp = function () {
  const data = {
    username: username.value,
    password1: password1.value,
    password2: password2.value,
    nickname: nickname.value,
    first_name: firstname.value.value,
    last_name: lastname.value.value,
    email: `${emailId.value}@${emailDomain.value}`,
    address: address.value,
    birth_date: birthDate.value,
    gender: gender.value,
    salary: salary.value,
    balance: balance.value,
  }
  console.log(data)
  axios({
    method: 'post',
    url: 'http://127.0.0.1:8000/accounts/signup/',
    data
  })
    .then(res => {
      console.log(res)
      router.push({name: 'welcome'})
    })
    .catch(err => {
      console.log(data)
      console.log(err)
    })
}
</script>

<style scoped>

</style>