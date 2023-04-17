<template>
  <div>

    <div class="row-1" style="display: flex; ">
      <div class="header2">
        <h2>Weather</h2>
      </div>
      <!-- <div>
        <label class="switch" style="top: 18px;">
          <input @input="darkMode = !darkMode, modeChange()" v-model="darkMode" type="checkbox">
          <span class="slider round"></span>
        </label>
      </div> -->
    </div>
    <div class="containter" style="padding: 10px 5px;">



      <div :style="[darkMode ? $store.state.dark : { color: 'black' }]" class="card-3" style="width: 30rem;">
        <h1 class="fw-bold mb-2 text-uppercase" style="
                  text-align: center;
                  padding-bottom: 10px;
                  padding-top: 4px;">Sign up</h1>
        <form @submit.prevent="signupUser">
          <div class="form-outline mb-4">
            <label for="validationCustom01" class="form-label">Name</label>
            <input type="text" class="form-control" id="validationCustom01" placeholder="Enter username"
              v-model="user.name" required>
          </div>
          <!-- Email input -->
          <div class="form-outline mb-4">
            <label class="form-label" for="form2Example1">Email address</label>
            <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp"
              placeholder="Enter email" v-model="user.email">
          </div>

          <!-- Password input -->
          <div class="form-outline mb-3">
            <label class="form-label" for="form2Example2">Password</label>
            <input type="password" class="form-control" id="exampleInputPassword1" v-model="user.password"
              placeholder="Password">

          </div>
          <div class="form-outline mb-4">
            <label class="form-label" for="typePhone">Phone number</label>
            <input type="tel" id="typePhone" class="form-control" placeholder="ex: 97 384 764" v-model="user.number" />
          </div>

          <div class="row mb-4">
            <!-- Submit button -->
            <button type="submit" class="button-34">Sign in</button>
          </div>
          <!-- Register buttons -->
          <div class="text-center">
            <p>or sign up with:</p>
            <button type="button" class="btn btn-link btn-floating mx-1">
              <i class="fab fa-facebook-f"></i>
            </button>

            <button type="button" class="btn btn-link btn-floating mx-1">
              <i class="fab fa-google"></i>
            </button>

            <button type="button" class="btn btn-link btn-floating mx-1">
              <i class="fab fa-twitter"></i>
            </button>

            <button type="button" class="btn btn-link btn-floating mx-1">
              <i class="fab fa-github"></i>
            </button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>

import { themeConfig } from '../EventBus'
import axios from 'axios';
import router from "../router";
export default {
  name: "SignUp",
  data() {
    return {
      darkMode: this.$store.state.darkmode,
      user: {
        name: "",
        email: "",
        password: "",
        number: "",
      },

    };
  },
  methods: {
    modeChange() {
      themeConfig.$emit('dark', this.darkMode);
      this.$store.commit('ChangeMode');
    },
    signupUser() {
      axios.post('http://localhost:3000/api/signup', {
        name: this.user.name,
        email: this.user.email,
        password: this.user.password,
        number: this.user.number
      })
        .then(response => {
          localStorage.setItem("username", this.user.name);
          localStorage.setItem("uidUser", response.data.insertedId);
          // console.log(response.data.insertedId);
          router.push("/user");

        })
        .catch(error => console.error(error));
    }
  }

}



</script>
<style>
.button-34 {
  background: #5E5DF0;
  border-radius: 999px;
  box-shadow: #5E5DF0 0 10px 20px -10px;
  box-sizing: border-box;
  color: #FFFFFF;
  cursor: pointer;
  font-family: Helvetica, "Apple Color Emoji", "Segoe UI Emoji", "Noto Color Emoji", "Segoe UI Symbol", "Android Emoji", EmojiSymbols, -apple-system, system-ui, "Segoe UI", Roboto, "Helvetica Neue", "Noto Sans", sans-serif;
  font-size: 16px;
  font-weight: 700;
  line-height: 24px;
  margin-left: 20px;
  opacity: 1;
  outline: 0 solid transparent;
  padding: 8px 18px;
  user-select: none;
  -webkit-user-select: none;
  touch-action: manipulation;
  width: 90%;
  word-break: break-word;
  border: 0;
}

.switch {
  position: relative;
  display: inline-block;
  width: 70px;
  height: 30px;
  margin: 0px;
  top: 0px;

}

.card-3 {
  width: 100%;
  height: 579px;
  background-color: white;
  border-radius: 25px;
  margin-top: 34px;
  padding: 13px;
}

.mb-4 {
  margin-bottom: 1.3rem !important;
}

.switch input {
  opacity: 0;
  width: 0;
  height: 0;
}

.slider {
  position: absolute;
  cursor: pointer;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  border: 2px;
  border-color: black;
  background-color: #1a5ec3;
  -webkit-transition: .4s;
  transition: .4s;
}

.slider:before {
  position: absolute;
  content: "";
  height: 20px;
  width: 20px;
  left: 4px;
  top: 2px;
  bottom: 4px;
  background-color: white;
  -webkit-transition: .4s;
  transition: .4s;
}

input:checked+.slider {
  background-color: #010103;
}

input:focus+.slider {
  box-shadow: 0 0 1px #010103;
}

input:checked+.slider:before {
  -webkit-transform: translateX(26px);
  -ms-transform: translateX(26px);
  transform: translateX(37px);
}

/* Rounded sliders */
.slider.round {
  border-radius: 34px;
  border-style: solid;
  border-width: 3px;
  border-color: #ffffff;
}

.slider.round:before {
  border-radius: 80%;

}
</style>
 