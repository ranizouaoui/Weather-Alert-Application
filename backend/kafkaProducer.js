
const kafka = require('kafka-node');
const Producer = kafka.Producer;
const client = new kafka.KafkaClient({ kafkaHost: process.env.KAFKA_HOST });
const producer = new Producer(client);
const axios = require('axios');
producer.on('ready', () => {
    console.log('Kafka Producer is connected and ready to send messages...');
});

producer.on('error', (error) => {
    console.error(`Error while connecting to Kafka: ${error}`);
});

async function sendWeatherData(city, type) {

    try {
        let weatherApiUrl = "";
        if (type == "daily") {
            weatherApiUrl = `https://api.openweathermap.org/data/2.5/weather?q=${city}&units=metric&appid=20571ab45c74dc2a1897b60c5b8047a1`;
        } else if (type == "hourly") {
            weatherApiUrl = `https://api.openweathermap.org/data/2.5/forecast?q=${city}&units=metric&appid=20571ab45c74dc2a1897b60c5b8047a1`;
        } else if (type == "seven") {
            weatherApiUrl = `https://api.openweathermap.org/data/2.5/forecast/daily?q=${city}&units=metric&appid=20571ab45c74dc2a1897b60c5b8047a1`;
        }
        const response = await axios.get(weatherApiUrl);
        const data = response.data;
        // console.log(data);
        const payloads = [
            {
                topic: 'weather',
                messages: JSON.stringify(data),
            }
        ];
        producer.send(payloads, (error, data) => {
            if (error) {
                console.error(`Error sending data to Kafka: ${error}`);
            } else {
                //  console.log(`Message sent to Kafka: ${JSON.stringify(data)}`);
                console.log(`Message sent to Kafka`);
            }
        });
    } catch (error) {
        console.error(`Error fetching weather data: ${error}`);
    }
}
async function sendWeatherDataByCoordinates(latitude, longitude, type) {

    try {
        let weatherApiUrl = "";
        if (type == "daily") {
            weatherApiUrl = `https://api.openweathermap.org/data/2.5/weather?lat=${latitude}&lon=${longitude}&units=metric&appid=20571ab45c74dc2a1897b60c5b8047a1`;
        } else if (type == "hourly") {
            weatherApiUrl = `https://api.openweathermap.org/data/2.5/forecast?lat=${latitude}&lon=${longitude}&units=metric&appid=20571ab45c74dc2a1897b60c5b8047a1`;
        } else if (type == "seven") {
            weatherApiUrl = `https://api.openweathermap.org/data/2.5/forecast/daily?lat=${latitude}&lon=${longitude}&units=metric&appid=20571ab45c74dc2a1897b60c5b8047a1`;
        }

        const response = await axios.get(weatherApiUrl);
        const data = response.data;
        const payloads = [
            {
                topic: 'weather',
                messages: JSON.stringify(data),
            }
        ];
        producer.send(payloads, (error, data) => {
            if (error) {
                console.error(`Error sending data to Kafka: ${error}`);
            } else {
                console.log(`Message sent to Kafka: ${JSON.stringify(data)}`);
            }
        });
    } catch (error) {
        console.error(`Error fetching weather data: ${error}`);
    }
}

module.exports = { sendWeatherData, sendWeatherDataByCoordinates };
