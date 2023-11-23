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

        <div class="me-3 input-group board-type-select">
          <span class="input-group-text" id="area">지역</span>
          <select class="form-select" name="area" id="area" v-model="areaInput">
            <option value="" disabled>지역 선택</option>
            <option value="all" v-if="cityInput">전체</option>
            <option v-for="area in areaObj[cityInput]" :value="area">{{ area }}</option>
          </select>
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
const birthDate = ref(null)
const gender = ref(1)
const salary = ref(null)
const balance = ref(null)
const cityInput = ref('')
const areaInput = ref('')

const cityList = [
  "서울특별시",
  "인천광역시",
  "대전광역시",
  "광주광역시",
  "대구광역시",
  "울산광역시",
  "부산광역시",
  "경기도",
  "강원도",
  "충청북도",
  "충청남도",
  "전라북도",
  "전라남도",
  "경상북도",
  "경상남도",
  "제주도"
]

const areaObj = {
    "서울특별시": ["강남구","강동구","강북구","강서구","관악구","광진구","구로구","금천구","노원구","도봉구","동대문구","동작구","마포구","서대문구","서초구","성동구","성북구","송파구","양천구","영등포구","용산구","은평구","종로구","중구","중랑구"],
    "인천광역시": ["계양구","남구","남동구","동구","부평구","서구","연수구","중구","강화군","옹진군"],
    "대전광역시": ["대덕구","동구","서구","유성구","중구"],
    "광주광역시": ["광산구","남구","동구", "북구","서구"],
    "대구광역시": ["남구","달서구","동구","북구","서구","수성구","중구","달성군"],
    "울산광역시": ["남구","동구","북구","중구","울주군"],
    "부산광역시": ["강서구","금정구","남구","동구","동래구","부산진구","북구","사상구","사하구","서구","수영구","연제구","영도구","중구","해운대구","기장군"],
    "경기도": ["고양시","과천시","광명시","광주시","구리시","군포시","김포시","남양주시","동두천시","부천시","성남시","수원시","시흥시","안산시","안성시","안양시","양주시","오산시","용인시","의왕시","의정부시","이천시","파주시","평택시","포천시","하남시","화성시","가평군","양평군","여주군","연천군"],
    "강원도": ["강릉시","동해시","삼척시","속초시","원주시","춘천시","태백시","고성군","양구군","양양군","영월군","인제군","정선군","철원군","평창군","홍천군","화천군","횡성군"],
    "충청북도": ["제천시","청주시","충주시","괴산군","단양군","보은군","영동군","옥천군","음성군","증평군","진천군","청원군"],
    "충청남도": ["계룡시","공주시","논산시","보령시","서산시","아산시","천안시","금산군","당진군","부여군","서천군","연기군","예산군","청양군","태안군","홍성군"],
    "전라북도": ["군산시","김제시","남원시","익산시","전주시","정읍시","고창군","무주군","부안군","순창군","완주군","임실군","장수군","진안군"],
    "전라남도": ["광양시","나주시","목포시","순천시","여수시","강진군","고흥군","곡성군","구례군","담양군","무안군","보성군","신안군","영광군","영암군","완도군","장성군","장흥군","진도군","함평군","해남군","화순군"],
    "경상북도": ["경산시","경주시","구미시","김천시","문경시","상주시","안동시","영주시","영천시","포항시","고령군","군위군","봉화군","성주군","영덕군","영양군","예천군","울릉군","울진군","의성군","청도군","청송군","칠곡군"],
    "경상남도": ["거제시","김해시","마산시","밀양시","사천시","양산시","진주시","진해시","창원시","통영시","거창군","고성군","남해군","산청군","의령군","창녕군","하동군","함안군","함양군","합천군"],
    "제주도": ["서귀포시","제주시","남제주군","북제주군"],
}

const signUp = function () {
  const data = {
    username: username.value,
    password1: password1.value,
    password2: password2.value,
    nickname: nickname.value,
    first_name: firstname.value.value,
    last_name: lastname.value.value,
    email: `${emailId.value}@${emailDomain.value}`,
    address: `${cityInput} ${areaInput}`,
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