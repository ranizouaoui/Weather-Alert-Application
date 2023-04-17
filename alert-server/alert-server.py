
# ?Description: 
# !This code defines a Flask server that listens for incoming POST requests on the /city endpoint.
# !When a request is received, the server retrieves a list of users registered in the specified city from a MongoDB database.
# !For each user, the server checks if the user exists in the database, retrieves the user's email and name, and sends an email
# !alert to the user if they are registered and if rain is expected in their city.

# TODO:
# ! ech mezeli , notifications menhebhomch yjou par email , heje mouch trend , donc naamlou push notification ! , wele yji sms khyyr
# ! Taarech kifeh , nejmou n5elliew choix lel user , wele naamlouha automatique (kenou connecté tjih push notification sinon sms)
# ! wele 3endi me5yyr , n5elliha lik enty ye developer e5dem solution elli thebha w aameli pull-request.

# libraries to use
import json
import requests
import smtplib
from bson import ObjectId
from datetime import datetime
from pymongo import MongoClient
from flask import Flask, request
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)

# Connect to the MongoDB server
client = MongoClient('mongodb://root:example@mongodb:27017/')
db = client['mydatabase']
cities = db['cities']
users = db['users']

# Define a route to receive data from the main server
@app.route('/city', methods=['POST'])
def send_emails_to_users():
    
    """
    Receives a cit  y name from the main server, retrieves the list of registered users
    in that city from MongoDB, and sends them an email alert if it's going to rain.
    """
    
    city_name = request.json
    get_users_data(city_name)
    return json.dumps(city_name), 200

def get_users_data(city_name):
    
    """
    Retrieves the list of users registered in the given city from MongoDB.
    """
    
    users_list = []
    for city in cities.find({'city': city_name}):
        users_list.append(city)
    get_data_from_users_collection(users_list)

def get_data_from_users_collection(users_list):
    
    """
    Sends an email alert to the given user if it's going to rain in their city.
    """
    
    for user in users_list:
        uid = user['uid']
        check_user = users.find_one({'_id': ObjectId(uid)})
        if check_user:
            print("User exists!")
            user['email']=check_user['email']
            user['name']=check_user['name']
            message ="Hello, "+user['name'].upper()+", It will rain today in "+user['city']+ " .take care of yourself!"
            send_email('noreplay.weather@gmail.com', user['email'], 'Weather alert', message, 'smtp.gmail.com', 587, 'noreplay.weather@gmail.com', 'glolaqiblwxrcnqf')
            
        else:
            # Weather data already exists, do nothing
            print("User does not exist!")

def send_email(sender_email, receiver_email, subject, body, smtp_server, smtp_port, username, password):
    # Create a multipart message and set headers
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = subject

    # Add body to email
    message.attach(MIMEText(body, 'plain'))

    # Create SMTP session for sending the mail
    try:
        session = smtplib.SMTP(smtp_server, smtp_port)
        session.starttls()
        session.login(username, password)
        text = message.as_string()
        session.sendmail(sender_email, receiver_email, text)
        session.quit()
        print('Email sent successfully : ',receiver_email)
    except Exception as e:
        print('Error: ' + str(e))
    # password : Weather123@
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000, debug=True)