

const kafka = require('kafka-node');
const client = new kafka.KafkaClient({ kafkaHost: process.env.KAFKA_HOST });
const Consumer = kafka.Consumer;
const consumer = new Consumer(
    client,
    [{ topic: 'weather', partition: 0 }],
    { autoCommit: true }
);

consumer.on('message', (message) => {
    const data = JSON.parse(message.value);
    // console.log(`Received message from Kafka: ${JSON.stringify(data)}`);
    console.log(`Received message from Kafka`);
});

consumer.on('error', (error) => {
    console.error(`Error while connecting to Kafka: ${error}`);
});

module.exports = { consumer };
