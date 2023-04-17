<template>
  <div class="containter" style="padding: 10px 5px;">
    <div style="    margin-left: auto;
                    margin-right: 15px;">
      <label class="switch">
        <input @input="darkMode = !darkMode, modeChange()" v-model="darkMode" type="checkbox">
        <span class="slider round"></span>
      </label>

      <router-link to="/SignIn"><img src="../assets/icons8_male_user_104px.png" alt style="width: 38px; height: 38px;     margin-left: 9px;
                                      margin-top: 6px;" /></router-link>
    </div>
    <br>
    <div class="header">
      <h1>Weather</h1>
    </div>

    <Search @showCards="showCard = true" @daily="getDaily" @seven="getSeven" />

    <Cards :daily="dailyData" :seven="sevenData" v-if="showCard" />
  </div>
</template>

<script>
import Cards from '../components/cards.vue'
import Search from '../components/search.vue'
import { themeConfig } from '../EventBus'


export default {
  name: "Home",
  components: { Cards, Search },
  data() {
    return {
      sevenData: [],
      dailyData: [],
      darkMode: this.$store.state.darkmode,
      showCard: true,

    };
  },
  methods: {
    modeChange() {
      themeConfig.$emit('dark', this.darkMode);
      this.$store.commit('ChangeMode');
    },
    getDaily(data) {
      this.dailyData = data
    },

    getSeven(data) {
      this.sevenData = data
    }

  },

}

</script>
<style>
.switch {
  position: relative;
  display: inline-block;
  width: 70px;
  height: 30px;
  margin: 0px;
  top: 0px;

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
 