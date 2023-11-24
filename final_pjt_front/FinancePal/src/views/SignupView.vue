<template>
  <div>
    <div class="form-group">
      <form @submit.prevent="signUpVal">
        <div class="header d-flex justify-content-between">
          <h3 class="mt-3">🔑 회원가입</h3>
          <button class="btn btn-success">제출</button>
        </div>
        <hr>
        <div class="input-group my-3">
          <span class="input-group-text">아이디</span>
          <input class="form-control" type="text" id="username" v-model="username" placeholder="*필수 값입니다*">
          <div class="input-group-append">
            <button class="btn btn-primary" type="button" @click="usernameVal">중복 확인</button>
          </div>
        </div>
        <p class="text-danger" v-if="usernameWarning">* 아이디 중복 확인을 해주세요.</p>

        <div class="input-group my-3">
          <span class="input-group-text">비밀번호</span>
          <input class="form-control" type="password" id="password1" v-model="password1" placeholder="*필수 값입니다*">
        </div>
        <div class="input-group my-3">
          <span class="input-group-text">비밀번호 확인</span>
          <input class="form-control" type="password" id="password2" v-model="password2" placeholder="*필수 값입니다*">
        </div>
        <p class="text-danger" v-if="password1Warning">* 비밀번호를 입력해주세요.</p>
        <p class="text-danger" v-else-if="password2Warning">* 비밀번호 확인을 해주세요.</p>
        <p class="text-danger" v-else-if="passwordEq">* 비밀번호가 일치하지 않습니다.</p>
        
        <div class="input-group my-3">
          <span class="input-group-text">성 (Last Name)</span>
          <input class="form-control" type="text" id="lastname" ref="lastname" placeholder="*필수 값입니다*">
        </div>
        <p class="text-danger" v-if="lastnameWarning">* 성을 입력해주세요.</p>

        <div class="input-group my-3">
          <span class="input-group-text">이름 (First Name)</span>
          <input class="form-control" type="text" id="firstname" ref="firstname" placeholder="*필수 값입니다*">
        </div>
        <p class="text-danger" v-if="firstnameWarning">* 이름을 입력해주세요.</p>

        <div class="input-group my-3">
          <span class="input-group-text">닉네임</span>
          <input class="form-control" type="text" id="nickname" v-model="nickname" placeholder="*필수 값입니다*">
          <div class="input-group-append">
            <button class="btn btn-primary" type="button" @click="nicknameVal">중복 확인</button>
          </div>
        </div>
        <p class="text-danger" v-if="nicknameWarning">* 닉네임을 확인해주세요.</p>
        
        <div class="input-group my-3">
          <span class="input-group-text">이메일</span>
          <input class="form-control" type="text" id="email-id" v-model="emailId">
          <span class="input-group-text"> @ </span>
          <select class="form-select" name="domain" id="domain" v-model="emailDomain">
            <option value="null" disabled>--선택--</option>
            <option v-for="email in emailList" :value="email">{{ email }}</option>
            <option value="etc">직접 입력</option>
          </select>
        </div>
        <div class="input-group my-3" v-if="emailDomain==='etc'">
          <span class="input-group-text" ref="emailInput">도메인을 입력해주세요</span>
          <input class="form-control" type="text" name="email-domain" id="email-domain">
        </div>
        <p class="text-danger" v-if="emailWarning">* 올바르지 않은 이메일 입니다.</p>

        <div class="me-3 input-group board-type-select">
          <span class="input-group-text" id="city">도시</span>
          <select class="form-select" name="city" id="city" v-model="cityInput">
            <option value="" disabled>도시 선택</option>
            <option v-for="city in cityList" :value="city">{{ city }}</option>
          </select>
          <span class="input-group-text" id="area">지역</span>
          <select class="form-select" name="area" id="area" v-model="areaInput">
            <option value="" disabled>지역 선택</option>
            <option v-for="area in areaObj[cityInput]" :value="area">{{ area }}</option>
          </select>
        </div>
        <p class="text-danger" v-if="cityWarning || areaWarning">* 주소를 입력해 주세요.</p>

        <div class="input-group my-3">
          <span class="input-group-text">생년월일</span>
          <input class="form-control" type="date" id="birth-date" v-model="birthDate">
        </div>
        <p class="text-danger" v-if="birthDateWarning">* 생년월일을 입력해주세요.</p>

        <div class="input-group my-3">
        <span class="input-group-text">성별</span>
          <select class="form-select" name="gender" id="gender" v-model="gender">
            <option value="1">남</option>
            <option value="0">여</option>
          </select>
        </div>

        <div class="input-group my-3">
          <span class="input-group-text">연봉</span>
          <input class="form-control" type="number" v-model="salary" placeholder="*필수 값입니다*">
        </div>
        <p class="text-danger" v-if="salaryWarning">* 연봉을 입력해주세요</p>

        <div class="input-group my-3">
          <span class="input-group-text">소지 금액</span>
          <input class="form-control" type="number" v-model="balance" placeholder="*필수 값입니다*">
        </div>
        <p class="text-danger" v-if="balanceWarning">* 소지 금액 입력해주세요.</p>
      </form>
    </div>
    </div>

</template>

<script setup>
import { ref, watch, computed } from 'vue'
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
const emailInput = ref(null)
const emailComputed = computed(() => {
  if (emailDomain.value === 'etc') {
    return emailInput.value.value
  } else {
    return emailDomain.value
  }
})
const birthDate = ref(null)
const gender = ref(1)
const salary = ref(null)
const balance = ref(null)
const cityInput = ref('')
const areaInput = ref('')

const emailList = [
  'naver.com',
  'gmail.com',
  'daum.net',
  'kakao.com',
]

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

const usernameWarning = ref(false)
const usernameConfirm = ref(true)
const usernameWatch = watch(username, () => {
    usernameConfirm.value = true
})
const usernameVal = function() {
  if (!username.value) {
    return
  }
  axios({
    method:'get',
    url: `http://127.0.0.1:8000/profile/username/validation/${username.value}`
  })
    .then(res => {
      const exists = res.data.exists
      if (exists) {
        window.alert('존재하는 아이디입니다.')
      } else {
        window.alert('사용 가능한 아이디입니다.')
        usernameConfirm.value = false
      }
    })
    .catch(err => {
      console.log(err)
    })
}

const nicknameWarning = ref(false)
const nicknameConfirm = ref(true)
const nicknameWatch = watch(username, () => {
    nicknameConfirm.value = true
})
const nicknameVal = function() {
  if (!nickname.value) {
    return
  }
  axios({
    method:'get',
    url: `http://127.0.0.1:8000/profile/nickname/validation/${nickname.value}`
  })
    .then(res => {
      const exists = res.data.exists
      if (exists) {
        window.alert('존재하는 닉네임입니다.')
      } else {
        window.alert('사용 가능한 닉네임입니다.')
        nicknameConfirm.value = false
      }
    })
    .catch(err => {
      console.log(err)
    })
}

const password1Warning = ref(false)
const password2Warning = ref(false)
const passwordEq = ref(false)
const lastnameWarning = ref(false)
const firstnameWarning = ref(false)
const cityWarning = ref(false)
const areaWarning = ref(false)
const birthDateWarning = ref(false)
const salaryWarning = ref(false)
const balanceWarning = ref(false)
const emailWarning = ref(false)

const password1Confirm = function() {
  if (!password1.value) {
    password1Warning.value = true
  }
}

const password2Confirm = function() {
  if (!password2.value) {
    password2Warning.value = true
  }
}

const passwordVal = function() {
  if (password1.value !== password2.value) {
    passwordEq = true
  }
}

const lastnameConfirm = function() {
  if (!lastname.value.value) {
    lastnameWarning.value =true
  }
}

const firstnameConfirm = function() {
  if (!firstname.value.value) {
    firstnameWarning.value = true
  }
}

const cityConfirm = function() {
  if (!cityInput.value) {
    cityWarning.value = true
  }
}

const areaConfirm = function() {
  if (!areaInput.value) {
    areaWarning.value = true
  }
}

const birthDateConfrim = function() {
  if (!birthDate.value) {
    birthDateWarning.value = true
  }
}

const salaryConfirm = function() {
  if (!salary.value) {
    salaryWarning.value = true
  }
}

const balanceConfirm = function() {
  if (!balance.value) {
    balanceWarning.value = true
  }
}

const emailVal = function() {
  if (emailId && !emailComputed) {
    emailWarning.value = true
  }
}

const signUpVal = function() {
  usernameWarning.value = usernameConfirm.value
  nicknameWarning.value = nicknameConfirm.value
  password1Warning.value = false
  password2Warning.value = false
  passwordEq.value = false
  lastnameWarning.value = false
  firstnameWarning.value = false
  cityWarning.value = false
  areaWarning.value = false
  birthDateWarning.value = false
  salaryWarning.value = false
  balanceWarning.value = false
  emailWarning.value = false
  
  password1Confirm()
  password2Confirm()
  passwordVal()
  lastnameConfirm()
  firstnameConfirm()
  cityConfirm()
  areaConfirm()
  birthDateConfrim()
  salaryConfirm()
  balanceConfirm()
  emailVal()

  if (
    usernameWarning.value||
    nicknameWarning.value||
    password1Warning.value||
    password2Warning.value||
    passwordEq.value||
    lastnameWarning.value||
    firstnameWarning.value||
    cityWarning.value||
    areaWarning.value||
    birthDateWarning.value||
    salaryWarning.value||
    balanceWarning.value||
    emailWarning.value
  ) {
    window.alert('올바르지 않은 입력이 있습니다.')
  } else {
    signUp()
  }

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
    address: `${cityInput.value} ${areaInput.value}`,
    birth_date: birthDate.value,
    gender: gender.value,
    salary: salary.value,
    balance: balance.value,
  }
  axios({
    method: 'post',
    url: 'http://127.0.0.1:8000/accounts/signup/',
    data
  })
    .then(res => {
      router.push({name: 'welcome'})
    })
    .catch(err => {
      console.log(err)
    })
}
</script>

<style scoped>
</style>