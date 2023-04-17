<template>
    <div>
        <h1>Get Weather Data</h1>
        <form @submit.prevent="getWeather">
            <input type="text" v-model="city" placeholder="Enter city name">
            <button type="submit">Get Weather</button>
        </form>
        <div v-if="weather">
            <h2>{{ weather.name }}</h2>
            <p>Temperature: {{ weather.main.temp }}°C</p>
            <p>Weather: {{ weather.weather[0].description }}</p>
        </div>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    data() {
        return {
            city: '',
            weather: null
        };
    },
    methods: {
        getWeather() {
            // try {
            //     const response = await axios.get(`/api/weather?city=${this.city}`);
            //     this.weather = response.data;
            // } catch (error) {
            //     console.error(error);
            // }
            axios.post('http://localhost:3000/api/weatherGeolocation', {
                latitude: 36.861118,
                longitude: 10.188034,
                type: "seven",
            }).then(response => {
                this.weather = response.data;
                console.log(response.data);

            })


        }
    }
};
</script>
