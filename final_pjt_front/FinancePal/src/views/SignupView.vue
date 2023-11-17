<template>
  <div>
    <h1>SignupView</h1>
    <form @submit.prevent="signUp">
      <p>User Name</p>
      <input type="text" id="username" v-model="username">
      <br>
      
      <p>Password</p>
      <input type="password" id="password1" v-model="password1">
      <br>
      
      <p>Password Comfirm</p>
      <input type="password" id="password2" v-model="password2">
      <br>

      <p>lastname</p>
      <input type="text" id="lastname" v-model="lastname">
      <br>

      <p>firstname</p>
      <input type="text" id="firstname" v-model="firstname">
      <br>

      <p>nickname</p>
      <input type="text" id="nickname" v-model="nickname">
      <br>

      <p>e-mail</p>
      <input type="text" id="email-id" v-model="emailId">
      <span> @ </span>
      <input type="text" id="email-domain" v-model="emailDomain">
      <br>

      <p>Address</p>
      <textarea name="address" id="address" cols="30" rows="10" v-model="address"></textarea>
      <br>

      <p>Birth Date</p>
      <input type="date" id="birth-date" v-model="birthDate">
      <br>

      <p>Gender</p>
      <select name="gender" id="gender" v-model="gender">
        <option value="1">남</option>
        <option value="0">여</option>
      </select>
      <br>
      
      <p>Salary</p>
      <input type="number" v-model="salary">
      <br>

      <p>Balance</p>
      <input type="number" v-model="balance">
      <br>
      <button>회원 가입</button>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'

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
    firstname: firstname.value,
    lastname: lastname.value,
    email: `${emailId.value}@${emailDomain}`,
    address: address.value,
    birthDate: birthDate.value,
    gender: gender.value,
    salary: salary.value,
    balance: balance.value,
  }
  
  axios({
    method:'post',
    url: 'http://127.0.0.1:8000/accounts/signup',
    data
  })
    .then(res => {
      console.log(res)
    })
    .catch(err => {
      console.log(err)
    })
}
</script>

<style scoped>

</style>