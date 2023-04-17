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
        <div style="justify-content: center;display: flex;">
          <div class="wrapper d-flex align-items-center">
            <div>
              <h1 class="fw-bold mb-2 text-uppercase" style="padding-top: 12px;">LOGIN</h1>
            </div>
          </div>
        </div>

        <form @submit.prevent="SignIn">
          <!-- Email input -->
          <div class="form-outline mb-2">
            <label for="form-label" class="col-form-label">Email address</label>
            <input type="email" class="form-control" id="form2Example" placeholder="Enter email" autocomplete="off"
              v-model="user.email">
          </div>

          <!-- Password input -->
          <div class="form-outline mb-4">
            <label for="form-label" class="col-sm-2 col-form-label">Password</label>

            <input type="password" class="form-control" id="inputPassword" placeholder="Enter password" autocomplete="off"
              v-model="user.password">

          </div>

          <!-- 2 column grid layout for inline styling -->
          <div class="row mb-4">
            <div class="col d-flex justify-content-center">
              <!-- Checkbox -->
              <div class="form-check">
                <input class="form-check-input" type="checkbox" value="" id="form2Example31" checked />
                <label class="form-check-label" for="form2Example31"> Remember me </label>
              </div>
            </div>

            <div class="col">
              <!-- Simple link -->
              <a href="#!" style="color:#0e59c8">Forgot password?</a>
            </div>
          </div>
          <div class="row mb-4">
            <!-- Submit button -->
            <button type="submit" class="button-34">Sign in</button>
          </div>


          <!-- Register buttons -->
          <div class="text-center">

            <p>Not a member? <router-link style="color:#0e59c8" to="/SignUp">Register</router-link></p>
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
  name: "SignIn",
  data() {
    return {
      darkMode: this.$store.state.darkmode,
      user: {
        email: "",
        password: "",
      },

    };
  },
  methods: {
    modeChange() {
      themeConfig.$emit('dark', this.darkMode);
      this.$store.commit('ChangeMode');
    },
    SignIn() {
      axios.post('http://localhost:3000/api/login', {
        email: this.user.email,
        password: this.user.password,
      })
        .then(response => {
          //  localStorage.setItem("uidUser", response.data.insertedId);
          console.log(response.data);
          localStorage.setItem("uidUser", response.data._id);
          localStorage.setItem("username", response.data.name);
          router.push("/user");

        })
        .catch(error => console.error(error));

    }
  },

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
  height: 520px;
  background-color: white;
  border-radius: 25px;
  margin-top: 34px;
  padding: 13px;
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
 