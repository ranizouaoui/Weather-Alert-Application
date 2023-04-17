<template>
  <div>
    <div :style="[darkMode ? $store.state.dark : { color: 'white' }]" class="card-1fav">
      <div class="cardsfav">
        <div class="today1fav">
          <h4 style="text-align: center;">{{ daily.name }}</h4>

          <div class="daily1fav">
            <img :src="require(`../assets/weater_elements/${weathers[daily.pic]}.svg`)" width="100px" alt />

            <p style="text-align: center;  font-size: 58px;margin-top: 10%;">{{ parseInt(daily.temp) }}°</p>
          </div>
          <br>
          <div class="wrapper d-flex align-items-stretch">
            <img src="../assets/delete.png" width="50px" @click="DeleteCity" />
            <img src="../assets/settings.png" width="46px" height="46" style="margin-top: 2px;" alt />
          </div>
        </div>

        <div>
        </div>
      </div>
    </div>
  </div>
</template>


<script>
import { themeConfig } from '../EventBus'
import axios from 'axios'
export default {
  name: 'CardFav',
  props: ['daily'],
  data() {
    return {

      darkMode: false,
      showCard: false,
      weathers: {
        Snow: "snowy",
        Clouds: "cloudy",
        Rain: "rainy",
        Clear: "sunny",
        Thunderstorm: "thunder",
      },
      days: ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'],
      daysIndex: [],

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
    async DeleteCity() {
      await this.$store.commit("removeFromCart", this.daily.name);
      axios.post('http://localhost:3000/api/deleteCity', {
        city: this.daily.name
      }).then(async response => {
        console.log(response.data);
        this.$store.commit("removeFromCart", this.daily.name);
        document.getElementById("favorites").click();
        document.getElementById("close1").click();
      }).catch(error => console.error(error));
    }
  },


}

</script>


<style>
.cardsfav {
  display: flex;
  width: 100%;
  margin-top: 3px;
  flex-direction: row;
  justify-content: space-around;
  align-items: center;
  flex-wrap: wrap;
}

.card-1fav {
  width: 92%;
  height: 270px;

  background-color: #4c9bcb;
  border-radius: 10px;
  margin-inline: auto;
  margin-top: 30px;
  padding: 10px;

}

.card-11fav {
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

.today1fav {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.todayDetails1fav {
  display: flex;
  margin-top: 14px;
  align-items: flex-start;
}

.daily1fav {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
}
</style>
 