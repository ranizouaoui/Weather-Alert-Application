<template>
    <div class="input" style="    width: 100% !important; padding-top: 50px;">
        <b-input-group class="input">
            <button class="inputpre" style="width: 50px; height: 50px;background: #f0f5ff;">
                <img src="../assets/search.png" alt />
            </button>

            <v-select class="vselect" placeholder="Search for location" v-model="selectedCity" @input="weatherLocation()"
                @search="onSearch" :options="cities" label="name" :filterable="false">
                <template slot="no-options">
                    <div class="rani" style="color: black;">

                        Type to search...
                    </div>
                </template>
                <template slot="option" slot-scope="option">
                    <div class="d-center">{{ option.name }}</div>
                </template>
                <template slot="selected-option" slot-scope="option">
                    <div class="selected d-center">
                        <div class="d-center">{{ option.name }}</div>
                    </div>
                </template>
            </v-select>

            <button @click="getLocation" class="inputpre" style="width: 50px; height: 50px;background: #f0f5ff;">
                <img src="../assets/target.png" alt />
            </button>

            <img src="../assets/icons8_github_512px.png" style="width: 45px; height: 45px;margin-top: auto;" alt />

        </b-input-group>
    </div>
</template>
<script>
import axios from 'axios'
import { themeConfig } from '../EventBus'

export default {

    data() {
        return {
            darkMode: false,
            selectedCity: "",
            cities: [],
            lat: "",
            lon: "",

        }

    },

    mounted() {
        themeConfig.$on('dark', (data) => {
            this.darkMode = data
        })

    },


    methods: {

        // City Search

        onSearch(search, loading) {
            this.cities = [];

            if (search.length) {
                loading(true);
                this.search(loading, search, this);
            }
        },
        search(loading, search) {
            // Set up request parameters
            const accessToken = 'pk.eyJ1IjoicmFuaXpvdWFvdWkiLCJhIjoiY2xlYWo0YTI1MHpzcjN3bWVibmRpbXBmOCJ9.MM2UU2ayrK7chiTHN3cLUg';
            const params = {
                access_token: accessToken,
                types: 'place'

            };
            axios.get('https://api.mapbox.com/geocoding/v5/mapbox.places/' + search + '.json', { params: params }).then(response => {
                loading(false);
                let cities = new Set();
                response.data.features.forEach(hit => {
                    cities.add(hit.text
                    );
                });
                //    console.log(response.data.features)
                this.cities = Array.from(cities);
            });
        },

        //With Select

        async weatherLocation() {
            let city = this.selectedCity;


            // await axios(`https://api.openweathermap.org/data/2.5/forecast/daily?q=${city}&units=metric&appid=20571ab45c74dc2a1897b60c5b8047a1`).then((res) => {
            //     this.$emit('seven', res.data)
            //     // console.log(res.data);
            // })
            await axios.post('http://localhost:3000/api/weather', {
                city: city,
                type: "seven",
            }).then(response => {
                this.$emit('seven', response.data)
                console.log(response.data);

            })
            // await axios(`https://api.openweathermap.org/data/2.5/weather?q=${city}&units=metric&appid=20571ab45c74dc2a1897b60c5b8047a1`).then((res) => {
            //     this.$emit('daily', res.data)
            // })
            await axios.post('http://localhost:3000/api/weather', {
                city: city,
                type: "daily",
            }).then(response => {
                this.$emit('daily', response.data)

            })
            // await axios(`https://api.openweathermap.org/data/2.5/forecast?q=${city}&units=metric&appid=20571ab45c74dc2a1897b60c5b8047a1`)
            //     .then((res) => {
            //         this.$emit('hourly', res.data);
            //     })
            await axios.post('http://localhost:3000/api/weather', {
                city: city,
                type: "hourly",
            }).then(response => {
                this.$emit('hourly', response.data)

            })
            this.$emit('showCards');


        },

        //With Geolocation

        async getGeolocation(data) {
            // await axios(`https://api.openweathermap.org/data/2.5/forecast/daily?lat=${data.coords.latitude}&lon=${data.coords.longitude}&units=metric&appid=20571ab45c74dc2a1897b60c5b8047a1`).then((res) => {
            //     this.$emit('seven', res.data)
            // });
            await axios.post('http://localhost:3000/api/weatherGeolocation', {
                latitude: data.coords.latitude,
                longitude: data.coords.longitude,
                type: "seven",
            }).then(response => {
                this.$emit('seven', response.data)

            })

            // await axios(`https://api.openweathermap.org/data/2.5/weather?lat=${data.coords.latitude}&lon=${data.coords.longitude}&units=metric&appid=20571ab45c74dc2a1897b60c5b8047a1`)
            //     .then((res) => {
            //         this.$emit('daily', res.data)
            //     })
            await axios.post('http://localhost:3000/api/weatherGeolocation', {
                latitude: data.coords.latitude,
                longitude: data.coords.longitude,
                type: "daily",
            }).then(response => {
                this.$emit('daily', response.data)

            })
            // await axios(`https://api.openweathermap.org/data/2.5/forecast?lat=${data.coords.latitude}&lon=${data.coords.longitude}&units=metric&appid=20571ab45c74dc2a1897b60c5b8047a1`)
            //     .then((res) => {
            //         this.$emit('hourly', res.data);
            //     })
            await axios.post('http://localhost:3000/api/weatherGeolocation', {
                latitude: data.coords.latitude,
                longitude: data.coords.longitude,
                type: "hourly",
            }).then(response => {
                this.$emit('daily', response.data)

            })
            this.$emit('showCards');

        },


        // Get User Location 
        getLocation() {
            if (navigator.geolocation) {
                navigator.geolocation.getCurrentPosition(data => {
                    //  console.log(data);
                    this.getGeolocation(data);
                    this.$emit('showCards');
                });
            }
            else {
                console.log("Geolocation is not supported by this browser.");
            }
        },
    }
}
</script>


<style>
.vselect .vs__search::placeholder,
.vselect .vs__dropdown-toggle {
    background: #f0f5ff;
    border: none;

    width: 100%;
    height: 50px;
    color: black;
}

.dark .vs__search::placeholder,
.dark .vs__dropdown-toggle,
.dark .vs__dropdown-menu {
    background: rgb(49, 50, 50);
    color: white !important;
    font-weight: 500;
    width: 100%;
}
</style>