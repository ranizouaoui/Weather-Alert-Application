
# ?Description: 
# !This code retrieves weather data from the OpenWeather API for a list of cities, sends the data to a Kafka topic,
# !and saves it to a MongoDB database. It uses the requests library to retrieve weather data from the OpenWeather API,
# !the KafkaProducer and KafkaConsumer classes from the kafka library to send and receive data to and from the Kafka 
# !topic,and the MongoClient class from the pymongo library to connect to and interact with the MongoDB database.

# libraries to use
import json
import requests
from kafka import KafkaProducer, KafkaConsumer
from pymongo import MongoClient
import datetime
import time

# OpenWeather API URL and API key
url = 'http://api.openweathermap.org/data/2.5/forecast'
api_key = '20571ab45c74dc2a1897b60c5b8047a1'

# Connect to the MongoDB server
client = MongoClient('mongodb://root:example@mongodb:27017/')
# Select the database and collection
db = client['mydatabase']

# Kafka topic to send/receive data
topic = 'weather_data'

# Kafka producer configuration
producer = KafkaProducer(bootstrap_servers=['kafka:9092'],
                         value_serializer=lambda x: json.dumps(x).encode('utf-8'))

# Kafka consumer configuration
consumer = KafkaConsumer(topic,
                         bootstrap_servers=['kafka:9092'],
                         auto_offset_reset='earliest',
                         enable_auto_commit=True,
                         group_id='my-group',
                         value_deserializer=lambda x: json.loads(x.decode('utf-8')))

# Function to retrieve weather data from OpenWeather API
def get_weather_data(city):
    params = {'q': city, 'appid': api_key, 'units': 'metric'}
    response = requests.get(url, params=params)
    return response.json()

# Function to send weather data to Kafka topic
def send_weather_data(city):
    data = get_weather_data(city)
    producer.send(topic, value=data)
    print(f"Weather data for {city} sent to Kafka topic {topic}")
    
def send_data_to_server(data):
    # Send a POST request to the other server
    url = 'http://analysis-servers:8000/process_data'
    response = requests.post(url, json=data)
    return response.json()
# Function to consume weather data from Kafka topic and save it to MongoDB
def consume_weather_data():
    while True:
        messages = consumer.poll(timeout_ms=1000)
        if not messages:
            print("No more messages to consume. Exiting...")
            break
        for message in messages.values():
            # Extract the city name and weather data from the Kafka message
            city_name = message[0].value['city']['name']
            weather_data = message[0].value
            # Send the data to the analysis server
            processed_data = send_data_to_server(weather_data)
            # Insert the weather data into MongoDB
            save_data(processed_data)

# Function to retrieve the list of cities from MongoDB
def get_cities():
    cities = db['cities']
    # Retrieve the list of cities
    city_list = []
    for city in cities.find():
        city_list.append(city['city'])
    return city_list

# Function to save weather data to MongoDB
def save_data(processed_data):
    data = db['weather_data']
    
    weather_data = processed_data['data']
    # Check if the weather data already exists
    existing_data = data.find_one({'city_name': processed_data['city_name'],'date': processed_data['date']})
    if existing_data is None:
        # Weather data does not exist, insert it into the collection
        result = data.insert_one(processed_data)
        print("Weather data inserted successfully!")
    else:
        # Weather data already exists, do nothing
        print("Weather data already exists.")

def main():
    # Set the time to run the code each day
    run_time = datetime.time(hour=13, minute=37, second=0)  # Set the time to run at 8:00am each day

    while True:
        # Get the current date and time
        now = datetime.datetime.now()

        # Calculate the number of seconds until the next run time
        time_until_run = datetime.datetime.combine(now.date(), run_time) - now

        # If the time to run the code has already passed today, wait until tomorrow to run it
        if time_until_run.total_seconds() < 0:
            time_until_run = datetime.timedelta(days=1) - time_until_run
        # Wait until it's time to run the code
        time.sleep(time_until_run.total_seconds())
        
        # Get the list of cities from MongoDB and send/receive weather data for each city
        # Run the code
        City_list = get_cities()
        for city in City_list:
            send_weather_data(city)
            consume_weather_data()

# if __name__ == '__main__':
#     main()
City_list = get_cities()
for city in City_list:
    send_weather_data(city)
    consume_weather_data()