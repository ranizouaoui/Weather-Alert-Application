<template>
    <div class="wrapper d-flex align-items-stretch">
        <div class="d-flex flex-column flex-shrink-0 bg-light" style="width: 4.5rem;">
            <a href="/" class="d-block p-3 link-dark text-decoration-none" title="Icon-only" data-bs-toggle="tooltip"
                data-bs-placement="right">
                <img src="../assets/icons8_snowflake_96px.png" alt style="width: 45px; height: 45px;" />
                <span class="visually-hidden">Icon-only</span>
            </a>
            <ul class="nav nav-pills nav-flush flex-column mb-auto text-center">
                <li class="nav-item">
                    <a @click="LoadHomePage()" class="nav-link active py-3 border-bottom" aria-current="page" title="Home"
                        data-bs-toggle="tooltip" data-bs-placement="right">
                        <img src="../assets/icons8_home_208px_1.png" alt style="width: 26px; height: 25px;" />
                    </a>
                </li>
                <li>
                    <a class="nav-link py-3 border-bottom" title="favorites" data-bs-toggle="tooltip" id="favorites"
                        data-bs-placement="right" @click="LoadFavoritesPage()">
                        <img src="../assets/icons8_favorite_cart_240px.png" alt style="width: 37px; height: 35px;" />
                    </a>
                </li>
                <li>
                    <a href="#" class="nav-link py-3 border-bottom" title="Orders" data-bs-toggle="tooltip"
                        data-bs-placement="right">
                        <svg class="bi" width="24" height="24" role="img" aria-label="Orders">
                            <use xlink:href="#table" />
                        </svg>
                    </a>
                </li>
                <li>
                    <a href="#" class="nav-link py-3 border-bottom" title="Products" data-bs-toggle="tooltip"
                        data-bs-placement="right">
                        <svg class="bi" width="24" height="24" role="img" aria-label="Products">
                            <use xlink:href="#grid" />
                        </svg>
                    </a>
                </li>
                <li>
                    <a href="#" class="nav-link py-3 border-bottom" title="Customers" data-bs-toggle="tooltip"
                        data-bs-placement="right">
                        <svg class="bi" width="24" height="24" role="img" aria-label="Customers">
                            <use xlink:href="#people-circle" />
                        </svg>
                    </a>
                </li>
            </ul>
        </div>
        <div class=" col-8" style="background-color: #f0f5ff;">
            <!-- <div v-if="loading" class="spinner-border text-secondary" role="status">
                <span class="visually-hidden">Loading...</span>
             </div> -->
            <div class="card2">

                <div class="row">
                    <div class="col">
                        <div style="margin: 15px;">
                            <h1 style="color: rgb(92 146 255);margin: 2px;">
                                {{ currentTime }}
                            </h1>
                            <p style="color: rgb(54 62 100);font-size: 16px;     margin-bottom: 0rem">
                                {{ currentDate }}
                            </p>
                            <div class="row">
                                <div class="col">
                                    <h2 style="color: rgb(92 146 255);">
                                        {{ greeting }}, {{ username }}!
                                    </h2>
                                </div>
                            </div>

                        </div>

                    </div>
                    <div class="col">
                        <div style="float: right;margin-top: 20px;margin-right: 70px;">
                            <label class="switch">
                                <input @input="darkMode = !darkMode, modeChange()" v-model="darkMode" type="checkbox">
                                <span class="slider round"></span>
                            </label>
                        </div>
                    </div>
                </div>
                <!-- there-->
                <div>
                    <div v-if="PageNum == 1">
                        <SevenDays :seven="sevenData" v-if="showCard" />
                        <!-- <PlanetChart :hourly="hourlyData" v-if="showCard" /> -->
                        <div v-if="showCard">
                            <div class="chart2" v-show="chart != null">
                                <div class="wrapper d-flex align-items-stretch">
                                    <h3 style="color: black; font-size: 21px;color: rgb(47 48 49);">Hourly Forecast</h3>
                                    <div style="margin-left: auto;margin-top: 2px; margin-right: 2px;">
                                        <div class="btn-group" role="group" aria-label="Basic radio toggle button group">
                                            <input type="radio" class="btn-check" name="btnradio" id="btnradio1"
                                                autocomplete="off" checked @input="ChartNum = 1, getData()">
                                            <label class="btn btn-outline-secondary" for="btnradio1">Temperature</label>

                                            <input type="radio" class="btn-check" name="btnradio" id="btnradio2"
                                                autocomplete="off" @input="ChartNum = 2, LoadPrecipitationData()">
                                            <label class="btn btn-outline-secondary" for="btnradio2">Rain</label>

                                            <input type="radio" class="btn-check" name="btnradio" id="btnradio3"
                                                autocomplete="off">
                                            <label class="btn btn-outline-secondary" for="btnradio3">Wind</label>
                                        </div>
                                    </div>
                                </div>

                                <canvas id="myChart"></canvas>
                            </div>
                        </div>
                    </div>
                    <div v-if="PageNum == 2">
                        <div>
                            <div class="card-favorite">
                                <h1 style="color: rgb(54, 62, 100);text-align: center;    font-family: cursive;">Manage
                                    Cities
                                </h1>
                                <div class="wrapper d-flex align-items-stretch" style="justify-content: center;">


                                    <!--    <DailyFavorites :daily="dailyData" />
                                    <DailyFavorites :daily="dailyData" />
                                    <DailyFavorites :daily="dailyData" />
                                    <DailyFavorites :daily="dailyData" /> -->
                                    <div v-for="city in mycities" :key="city.id">
                                        <DailyFavorites :daily="city" />
                                    </div>

                                </div>
                                <br>
                                <nav aria-label="Page navigation example" v-if="mycities.length > 4">
                                    <ul class="pagination justify-content-center">
                                        <li class="page-item disabled">
                                            <a class="page-link" href="#" tabindex="-1">Previous</a>
                                        </li>
                                        <li class="page-item"><a class="page-link" href="#">1</a></li>
                                        <li class="page-item"><a class="page-link" href="#">2</a></li>
                                        <li class="page-item"><a class="page-link" href="#">3</a></li>
                                        <li class="page-item">
                                            <a class="page-link" href="#">Next</a>
                                        </li>
                                    </ul>
                                </nav>
                            </div>
                        </div>
                    </div>
                </div>
                <!-- there-->
                <br>
                <br>
            </div>
            <!-- <i class="fab fa-github fa-2x" style="color: #333333;"></i> -->
        </div>
        <div class="col" style="background-color:white ;right: 0px; width: 28%;">
            <div class="card1">
                <Search @showCards="showCard = true" @daily="getDaily" @seven="getSeven" v-on:hourly="getHourly" />
                <DailyCard :daily="dailyData" />
            </div>
        </div>
    </div>
</template>

<script>
import Chart from 'chart.js'
import SevenDays from '../components/SevenDays.vue'
import Search from '../components/search-user.vue'
import DailyCard from '../components/DailyCard.vue'
import DailyFavorites from '../components/CardFavorites.vue'
import { themeConfig } from '../EventBus'
import axios from 'axios'
export default {
    name: "User",
    components: { SevenDays, Search, DailyCard, DailyFavorites },

    data() {
        return {
            sevenData: [],
            dailyData: [],
            hourlyData: [],
            darkMode: this.$store.state.darkmode,
            showCard: true,
            chart: null,
            city: "tunis",
            dates: [],
            temps: [],
            currentDate: new Date().toLocaleDateString('en-US', { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' }),
            ChartNum: 1,
            PageNum: 1,
            loading: true,
            mycities: [],
            numcities: 0,
            uid: localStorage.getItem("uidUser"),
            time: new Date(),
            username: localStorage.getItem("username"),
        }
    },
    methods: {
        modeChange() {
            themeConfig.$emit('dark', this.darkMode);
            this.$store.commit('ChangeMode');
        },
        getDaily(data) {
            this.dailyData = data;
        },

        getSeven(data) {
            this.sevenData = data
        },
        getHourly(data) {
            this.hourlyData = data
        },
        //With Geolocation

        async getGeolocation(data) {
            this.loading = true;
            // await axios(`https://api.openweathermap.org/data/2.5/forecast/daily?lat=${data.coords.latitude}&lon=${data.coords.longitude}&units=metric&appid=20571ab45c74dc2a1897b60c5b8047a1`).then((res) => {
            //     //  this.$emit('seven', res.data)
            //     this.sevenData = res.data;
            // });
            await axios.post('http://localhost:3000/api/weatherGeolocation', {
                latitude: data.coords.latitude,
                longitude: data.coords.longitude,
                type: "seven",
            }).then(response => {
                this.sevenData = response.data;

            })
            // await axios(`https://api.openweathermap.org/data/2.5/weather?lat=${data.coords.latitude}&lon=${data.coords.longitude}&units=metric&appid=20571ab45c74dc2a1897b60c5b8047a1`)
            //     .then((res) => {
            //         //  this.$emit('daily', res.data)
            //         this.dailyData = res.data;
            //     })
            await axios.post('http://localhost:3000/api/weatherGeolocation', {
                latitude: data.coords.latitude,
                longitude: data.coords.longitude,
                type: "daily",
            }).then(response => {
                this.dailyData = response.data;

            })
            // await axios(`https://api.openweathermap.org/data/2.5/forecast?lat=${data.coords.latitude}&lon=${data.coords.longitude}&units=metric&appid=20571ab45c74dc2a1897b60c5b8047a1`)
            //     .then((res) => {
            //         this.hourlyData = res.data;
            //     })
            await axios.post('http://localhost:3000/api/weatherGeolocation', {
                latitude: data.coords.latitude,
                longitude: data.coords.longitude,
                type: "hourly",
            }).then(response => {
                this.hourlyData = response.data;

            })
            this.loading = false;
            this.getData();
            this.$emit('showCards');

        },


        // Get User Location 
        getLocation() {
            if (navigator.geolocation) {
                navigator.geolocation.getCurrentPosition(data => {
                    console.log(data);
                    this.getGeolocation(data);
                    //  this.$emit('showCards');
                });
            }
            else {
                console.log("Geolocation is not supported by this browser.");
            }
        },
        getData() {
            if (this.chart != null) {
                this.chart.destroy();
            }
            // console.log(response.data.list);
            this.dates = this.hourlyData.list.map(list => {
                return list.dt_txt;
            });

            this.temps = this.hourlyData.list.map(list => {
                return list.main.temp;
            });

            var ctx = document.getElementById("myChart");
            this.chart = new Chart(ctx, {
                type: "line",
                data: {
                    labels: this.dates,
                    datasets: [
                        {
                            label: "Avg. Temp",
                            backgroundColor: "#a3d8fc",
                            borderColor: "#5aa5f3",
                            borderWidth: 3,
                            data: this.temps
                        }
                    ]
                },
                options: {
                    title: {
                        display: true,
                        text: "Temperature per 3 hour"
                    },
                    tooltips: {
                        callbacks: {
                            label: function (tooltipItem, data) {
                                var label =
                                    data.datasets[tooltipItem.datasetIndex].label || "";

                                if (label) {
                                    label += ": ";
                                }

                                label += Math.floor(tooltipItem.yLabel);
                                return label + "°C";
                            }
                        }
                    },
                    scales: {
                        xAxes: [
                            {
                                type: "time",
                                time: {
                                    unit: "hour",
                                    displayFormats: {
                                        hour: "ddd hA"
                                    },
                                    tooltipFormat: "ddd hA"
                                },
                                scaleLabel: {
                                    display: true,
                                    labelString: "Time"
                                }
                            }
                        ],
                        yAxes: [
                            {
                                scaleLabel: {
                                    display: true,
                                    labelString: "Temperature (°C)"
                                },
                                ticks: {
                                    callback: function (value) {
                                        return value + "°C";
                                    }
                                }
                            }
                        ]
                    }
                }
            });

        },
        LoadPrecipitationData() {

            if (this.chart != null) {
                this.chart.destroy();
            }
            // console.log(response.data.list);
            this.dates = this.hourlyData.list.map(list => {
                return list.dt_txt;
            });

            this.temps = this.hourlyData.list.map(list => {
                return (list.rain ? list.rain['3h'] : 0);
            });

            var ctx = document.getElementById("myChart");
            this.chart = new Chart(ctx, {
                type: "line",
                data: {
                    labels: this.dates,
                    datasets: [
                        {
                            label: "Avg. Rain",
                            backgroundColor: "#a3d8fc",
                            borderColor: "#5aa5f3",
                            borderWidth: 3,
                            data: this.temps
                        }
                    ]
                },
                options: {
                    title: {
                        display: true,
                        text: "Precipitation per 3 hour"
                    },
                    tooltips: {
                        callbacks: {
                            label: function (tooltipItem, data) {
                                var label =
                                    data.datasets[tooltipItem.datasetIndex].label || "";

                                if (label) {
                                    label += ": ";
                                }

                                label += Math.floor(tooltipItem.yLabel);
                                return label + "%";
                            }
                        }
                    },
                    scales: {
                        xAxes: [
                            {
                                type: "time",
                                time: {
                                    unit: "hour",
                                    displayFormats: {
                                        hour: "ddd hA"
                                    },
                                    tooltipFormat: "ddd hA"
                                },
                                scaleLabel: {
                                    display: true,
                                    labelString: "Time"
                                }
                            }
                        ],
                        yAxes: [
                            {
                                scaleLabel: {
                                    display: true,
                                    labelString: "Rain (%)"
                                },
                                ticks: {
                                    callback: function (value) {
                                        return value + "%";
                                    }
                                }
                            }
                        ]
                    }
                }
            });
        },
        LoadHomePage() {
            this.PageNum = 1;
            this.getData();
        },
        LoadFavoritesPage() {
            this.PageNum = 2;
            this.LoadCities();
        },
        LoadCities() {
            this.mycities = [];
            axios.post('http://localhost:3000/api/cities', {
                uid: this.uid
            }).then(async response => {
                // console.log(response.data);
                this.numcities = response.data.length;
                for (let index = 0; index < response.data.length; index++) {
                    await axios(`https://api.openweathermap.org/data/2.5/weather?q=${response.data[index].city}&units=metric&appid=20571ab45c74dc2a1897b60c5b8047a1`).then((res) => {
                        this.mycities.push({
                            name: res.data.name,
                            temp: res.data.main.temp,
                            pic: res.data.weather[0].main,
                            id: response.data[index]._id

                        })
                    })
                }
            }).catch(error => console.error(error));
        }
    },
    created() {
        this.getLocation();


    },
    watch: {
        hourlyData() {
            if (this.ChartNum == 1) {

                this.getData();
            } else {
                this.LoadPrecipitationData();
            }

        },
        dailyData() {
            this.$store.commit("DisplayAdd");
            this.$store.state.cart.forEach(item => {
                if (item == this.dailyData.name) {
                    this.$store.commit("DisplayCheck");
                }

            });
        }
    },
    computed: {
        currentTime() {
            return this.time.toLocaleTimeString('en-US')
        },
        greeting() {
            const hours = this.time.getHours()
            if (hours >= 6 && hours < 18) {
                return 'Good Morning'
            } else {
                return 'Good Night'
            }
        }
    },
    mounted() {
        setInterval(() => {
            this.time = new Date()
        }, 1000)
    }

}
</script>
<style>
.card1 {
    width: 100%;
    margin-left: auto;
    min-height: 100vh;
    background-color: white;
}

.card-favorite {
    width: 90%;
    min-height: 65vh;
    background-color: white;
    margin-top: 30px;
    padding: 10px;
    border-radius: 10px;
    margin-left: 3%;


}

.card2 {

    min-height: 100vh;
    width: 104%;
    min-height: 100vh;
    background-color: #f0f5ff;
}

.switch {
    position: relative;
    display: inline-block;
    width: 70px;
    height: 32px;
    margin: 0px;
    top: 0px;

}

.switch input {
    opacity: 0;
    width: 0;
    height: 0;
}

.chart2 {
    margin-top: 30px;
    padding: 10px;
    background-color: white;
    border-radius: 10px;
    margin-left: 3%;
    height: 460px;
    width: 90%;

}

.slider {
    position: absolute;
    cursor: pointer;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    border: 1px;
    border-color: black;
    background-color: #ffffff;
    -webkit-transition: .4s;
    transition: .4s;
}

.slider:before {
    position: absolute;
    content: "";
    height: 20px;
    width: 20px;
    left: 4px;
    top: 3px;
    bottom: 4px;
    background-color: #6498FF;
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