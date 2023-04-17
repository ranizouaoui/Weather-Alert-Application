
# ?Description: 
# !This code defines a web server using the Flask library that receives weather data from a main server via a POST request.
# !The weather data is processed to check if there is any rain during the day, and if so, the name of the city is sent to an
# !alert server using a separate HTTP request. The processed data, including a flag indicating whether it's a rainy day or not,
# !is then returned to the main server as a JSON object.

# libraries to use
import json
import requests
from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

# Define a route to receive data from the main server
@app.route('/process_data', methods=['POST'])
def process_data():
    # Receive the data from the main server
    data = request.json
    # Process the data (check for rain)
    if is_rainy_day(data):
        # If it's a rainy day, add a key-value pair to the data indicating that
        data['is_rainy_day'] = True
    else:
        # If it's not a rainy day, add a key-value pair to the data indicating that
        data['is_rainy_day'] = False
    
    # Add the current date to the data
    date = datetime.now().strftime('%Y-%m-%d')
    
    # Send the processed data back to the main server
    response = {
        'city_name':data['city']['name'],
        'data': data,
        'date': date
    }
    return json.dumps(response), 200

# Function to check if there is rain during the day
def is_rainy_day(data):
    # Get the list of hourly weather data
    hourly_data = data['list']
    
    # Loop through each hour's weather data
    for hour in hourly_data:
        # Get the weather conditions for this hour
        weather = hour['weather'][0]
        
        # If the weather description contains the word "rain" (case insensitive)
        if 'rain' in weather['description'].lower():
            # Send the city name to an alert server
            city_sended = send_city_name_to_alert_server(data['city']['name'])
            # Return True to indicate that it's a rainy day
            return True
    
    # If no rainy hours were found, return False to indicate that it's not a rainy day
    return False

# Function to send the city name to an alert server
def send_city_name_to_alert_server(city):
    # Send a POST request to the other server with the city name as JSON data
    url = 'http://alert-server:9000/city'
    response = requests.post(url, json=city)
    
    # Return the response from the alert server as a JSON object
    return response.json()
    
if __name__ == '__main__':
    # Run the Flask app on localhost:8000 with debug mode enabled
    app.run(host='0.0.0.0', port=8000, debug=True)
