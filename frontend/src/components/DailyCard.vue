<template>
  <div>
    <div :style="[darkMode ? $store.state.dark : { color: 'white' }]" class="card-1">
      <div class="cards">
        <div class="today1">
          <h3 style="text-align: center;">{{ daily.name }}</h3>

          <div class="daily1">
            <img :src="require(`../assets/weater_elements/${weathers[daily.weather[0].main]}.svg`)" width="190px" alt />

            <p style="text-align: center;  font-size: 70px;margin-top: 10%;">{{ parseInt(daily.main.temp) }}°</p>
          </div>
          <h2>{{ daily.weather[0].main }}</h2>
          <br>
          <br>
        </div>
        <!-- 
      <div class="todayDetails1">
     <h3>Feels Like {{ parseInt(daily.main.feels_like) }}°</h3> 
        <h3>
          <img width="64" src="../assets/weater_elements/humity.png" alt />
          {{ daily.main.humidity }}%
        </h3>
        <h3>
          <img src="../assets/weater_elements/down.png" alt />
          {{ parseInt(daily.main.temp_min) }}°
        </h3>

        <h3>
          <img src="../assets/weater_elements/up.png" alt />
          {{ parseInt(daily.main.temp_max) }}°
        </h3>
        <h3>
          <img src="../assets/weater_elements/wind.png" alt />
          {{ daily.wind.speed }} km/h
        </h3>
      </div> -->
        <div>
          <div class="row" style="height: 20px; --bs-gutter-x: 0rem;">
            <div class="col" style="width: 47px;">
              <div class="wrapper d-flex">
                <img src="../assets/icons8_wind_50px.png"
                  style="width: 20px; height: 20px; margin-top: 2px; margin-right: 2px;" alt />
                <p> Wind: </p>
              </div>

            </div>
            <div class="col" style="width: 47px;">
              <p>{{ daily.wind.speed }} Km/h</p>
            </div>
            <div class="w-100"></div>
            <div class="col" style="width: 47px;">
              <div class="wrapper d-flex">
                <img src="../assets/icons8_humidity_50px.png"
                  style="width: 20px; height: 20px; margin-top: 2px;margin-right: 2px;" alt />
                <p> Hum:</p>
              </div>

            </div>
            <div class="col" style="width: 47px;">
              <p>{{ daily.main.humidity }}%</p>
            </div>
          </div>
        </div>

      </div>
      <br>
      <br>
      <div style="margin-top: 20px;">
        <div id="buttonAdd" :style="{ display: textdisplay }"> <button type="button" class="btn btn-outline-light"
            style="width: 100%;border-radius: 20px;" data-bs-toggle="modal" data-bs-target="#exampleModal">Add to
            favorites</button>
        </div>
        <div id="buttonManage" :style="{ display: textdisplay1 }"> <button type="button" class="btn btn-outline-light"
            style="width: 100%;border-radius: 20px;" @click="GoToCart">Manage your
            favorites Cites</button>
        </div>

      </div>

    </div>

    <div class="card-11">
      <div class="row" style="    padding-top: inherit;">
        <div class="col">
          <div class="wrapper d-flex align-items-stretch">
            <img src="../assets/sun-new.png" style="width: 50px; height: 52px; margin-top: auto; margin-right: 2px;"
              alt />
            <div>
              <h6 style="color: #C3C8DE;">Sunrise</h6>
              <h6 style="color: #5C92FF;"> {{ new Date(this.daily.sys.sunrise * 1000).toLocaleTimeString('en-US') }}
              </h6>
            </div>

          </div>

        </div>
        <div class="col">
          <div class="wrapper d-flex " style="  display: flex;
                        flex-direction: row;
                        align-items: center;
                        justify-content: center;">
            <img src="../assets/moon.png" style="width: 40px; height: 40Spx; margin-right: 2px;" alt />
            <div>
              <h6 style="color: #C3C8DE;">Sunset </h6>
              <h6 style="color: #5C92FF;"> {{ this.sunset = new Date(this.daily.sys.sunset *
                1000).toLocaleTimeString('en-US') }}</h6>
            </div>
          </div>

        </div>
      </div>


    </div>
    <!-- Modal -->
    <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="exampleModalLabel" style="color:black;">Add to favorites</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            <div class="alert alert-secondary" role="alert">
              You will receive notifications about the weather condition. you can always configure or schedule the time to
              send notifications in the settings. We will send notifications automatically in case you did not plan the
              sending time
            </div>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" id="close" data-bs-dismiss="modal">Close</button>
            <button type="button" class="btn btn-success" @click="AddTofavorites">Save changes</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>


<script>
import { themeConfig } from '../EventBus'
import axios from 'axios';
export default {
  name: 'Cards',
  props: ['daily'],
  data() {
    return {

      darkMode: false,
      showCard: false,
      displaycheck: this.$store.state.DisplayCheck,
      weathers: {
        Snow: "snowy",
        Clouds: "cloudy",
        Rain: "rainy",
        Clear: "sunny",
        Thunderstorm: "thunder",
      },
      days: ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'],
      daysIndex: [],
      uid: localStorage.getItem("uidUser"),

    };
  },
  mounted() {
    themeConfig.$on('dark', (data) => {
      this.darkMode = data
    })

    var currentDate = new Date();
    var nextWeek = new Date(currentDate.getTime() + 7 * 24 * 60 * 60 * 1000);
    var days = []
    while (currentDate <= nextWeek) {
      days.push(new Date(currentDate).getDay());
      currentDate.setDate(currentDate.getDate() + 1);
    }
    this.daysIndex = days.slice(1);


  },
  methods: {
    addToCart(item) {
      console.log(item);
      //this.$store.commit("addToCart", item);
    },
    AddTofavorites() {
      //  var element = document.getElementById("buttonAdd");
      //  var element1 = document.getElementById("buttonManage");
      axios.post('http://localhost:3000/api/AddTofavorites', {
        city: this.daily.name,
        uid: this.uid
      })
        .then(response => {
          // console.log(response.data.insertedId);
          // element.style.display = "none";
          // element1.style.display = "block";
          //  this.addToCart(this.daily.name);
          console.log(this.daily.name)
          this.$store.commit("addToCart", this.daily.name);
          this.$store.commit("DisplayCheck");
          document.getElementById("favorites").click();
          document.getElementById("close").click();
          console.log(response.data)
          // router.push("/user");

        })
        .catch(error => console.error(error));
    },
    GoToCart() {
      document.getElementById("favorites").click();
    }
  },
  computed: {
    textdisplay() {
      // assuming that `state.value` is a Vuex store state
      return this.$store.state.DisplayCheck == true ? 'none' : 'block';
    },
    textdisplay1() {
      // assuming that `state.value` is a Vuex store state
      return this.$store.state.DisplayCheck == true ? 'block' : 'none';
    }
  }


}

</script>


<style>
.cards {
  display: flex;
  width: 100%;
  margin-top: 3px;
  flex-direction: row;
  justify-content: space-around;
  align-items: center;
  flex-wrap: wrap;
}

.card-1 {
  width: 83%;
  height: 490px;
  background-color: #5aa5f3;
  border-radius: 10px;
  margin-inline: auto;
  margin-top: 50px;
  padding: 10px;

}

.card-11 {
  width: 82%;
  height: 100px;
  background-color: #fff8f0;
  border-radius: 10px;
  margin-inline: auto;
  border-style: dashed;
  border-color: #ffe4b8;
  border-width: 2px;
  color: #C3C8DE;
  margin-top: 20px;
  padding: 10px;
}

.today1 {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.todayDetails1 {
  display: flex;
  margin-top: 14px;
  align-items: flex-start;
}

.daily1 {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
}
</style>
 