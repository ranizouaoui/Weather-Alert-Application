const express = require('express')
const { MongoClient } = require('mongodb')
const bodyParser = require('body-parser');
const cors = require("cors");
const kafkaProducer = require('./kafkaProducer');
const { consumer } = require('./kafkaConsumer');
///const MONGODB_URL = process.env.MONGODB_URL || 'mongodb://localhost:27017/mydatabase'
const app = express()
app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());
app.use(cors());
// ! Use this link if you work in docker : mongodb://root:example@mongodb:27017/mydatabase?authSource=admin
// ! Use this link if you work in localhost: mongodb://root:example@localhost:27017/mydatabase?authSource=admin
const client = new MongoClient('mongodb://root:example@mongodb:27017/mydatabase?authSource=admin', { useUnifiedTopology: true })
const db = client.db('mydatabase');
const collection = db.collection('users');
const cities = db.collection('cities');
client.connect().then(() => {
    console.log('Connected to MongoDB')
}).catch(error => {
    console.error(error)
})

app.get('/', (req, res) => {
    res.send('Hello World!')
})
app.post('/api/signup', async (req, res) => {
    const { name, email, password, number } = req.body;

    try {
        const result = await collection.insertOne({ name, email, password, number });
        console.log(result);
        //client.close();
        res.status(200).send(result);
    } catch (err) {
        console.error(err);
        res.status(500).send({ message: 'Failed to create user' });
    }
});
app.post('/api/login', async function (req, res) {
    const { email, password } = req.body;
    const result = await collection.findOne({ email: email, password: password });
    if (result) {
        res.status(200).send(result);
        // console.log(result)
    } else {
        res.status(500).send({ auth: false, data: 'Failed' });
    }

});
app.post('/api/cities', async function (req, res) {
    const { uid } = req.body;
    // Find cities based on uid
    const result = await cities.find({ uid: uid }).toArray();
    console.log(result);
    res.json(result);
});
app.post('/api/AddTofavorites', async function (req, res) {
    const { city, uid } = req.body;
    const result = await cities.insertOne({ city, uid });
    if (result) {
        res.status(200).send(result);
        // console.log(result._id)
    } else {
        res.status(500).send({ auth: false, data: 'Failed' });
    }

});
app.post('/api/deleteCity', async function (req, res) {
    const { city } = req.body;
    const result = await cities.deleteOne({ city: city });
    res.status(200).send(`Successfully deleted city with id`);
    console.log(result);

});
// API endpoint to get weather data for a city
app.post('/api/weather', async function (req, res) {
    const { city, type } = req.body;
    let receivedMessages = 0;
    let expectedMessages = 1; // Assuming we only expect one message for now
    // Send city name to Kafka producer
    kafkaProducer.sendWeatherData(city, type);

    // Wait for data to be received from Kafka consumer
    consumer.on('message', (message) => {
        const weatherData = JSON.parse(message.value);
        console.log(weatherData);
        receivedMessages++;
        if (receivedMessages === expectedMessages) {
            // We have received all the messages we expect, so send the response
            res.status(200).send(weatherData);
        }
    });
});
// API endpoint to get weather data for a  city using Geolocation
app.post('/api/weatherGeolocation', async function (req, res) {
    const { latitude, longitude, type } = req.body;
    let receivedMessages = 0;
    let expectedMessages = 1; // Assuming we only expect one message for now
    // Send Geolocation position  to Kafka producer
    kafkaProducer.sendWeatherDataByCoordinates(latitude, longitude, type);

    // Wait for data to be received from Kafka consumer
    consumer.on('message', (message) => {
        const weatherData = JSON.parse(message.value);
        console.log(weatherData);
        receivedMessages++;
        if (receivedMessages === expectedMessages) {

            res.status(200).send(weatherData);
        }

    });
});
app.listen(3000, () => {
    console.log('Server started on port 3000')
})
