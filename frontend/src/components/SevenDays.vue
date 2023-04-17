<template>
  <div :style="[darkMode ? $store.state.dark : { color: 'black' }]" class="card-2">


    <div class="daysDetail">
      <span style="display:flex; flex-direction:column; align-items:center; padding-left:10px" v-for="data in seven.list"
        :key="data">
        <p>
          {{ data.day }}
        </p>
        <img :src="require(`../assets/weater_elements/${weathers[data.weather[0].main]}.svg`)" width="100px" alt />
        <p>{{ data.weather[0].main }}</p>
        <p>{{ parseInt(data.temp.day) }}° / {{ parseInt(data.temp.night) }}°</p>
      </span>
    </div>
  </div>
</template>


<script>
import { themeConfig } from '../EventBus'
export default {
  name: 'SevenDays',
  props: ['seven'],
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
  watch: {
    seven: function () {
      for (let i = 0; i < this.daysIndex.length; i++) {
        this.seven.list[i].day = this.days[this.daysIndex[i]]

      }

    }
  }


}

</script>


<style>
.todayDetails {
  display: flex;
  margin-top: 10px;
  flex-direction: column;
  align-items: flex-start;
}

.card-2 {
  width: 90%;
  height: 300px;
  background-color: white;
  border-radius: 10px;
  margin-top: 20px;
  padding: 20px;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: stretch;
  margin-inline: 3%;
  justify-content: center;
  overflow: auto;
}

.days {
  display: flex;
  flex-direction: row;
  justify-content: space-around;
  font-size: 23px;
}

.daysDetail {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-around;
  font-size: 23px;
}

@media (max-width: 1300px) {
  .card-2 {
    align-items: baseline;
  }

  .results {
    width: 90vw !important;
  }

}
</style>
 