import requests
import os
from dotenv import load_dotenv
from twilio.rest import Client  # Download helper library from Twilio

load_dotenv(".env")  # loads the environment file

api_key = os.getenv("OWM_API_KEY")  # api key
account_sid = os.getenv("ACCOUNT_SID")  # account sid
auth_token = os.getenv("AUTH_TOKEN")  # auth token

parameters = {  # parameters to be passed, the geographical coordinates are set to the location of Longueuil, Canada
    "lat": 45.533852,
    "lon": -73.515213,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=parameters)  # GET request to OWM
response.raise_for_status()  # raises exception if GET request is invalid
weather_data = response.json()  # parses the response from the API

weather_list = [weather_data['hourly'][n]['weather'][0]['id'] for n in range(12)]  # taps into the data and fetches the
# weather id for the first 12 hours of the day


will_rain = False

for condition_code in weather_list:  # check for all the condition code
    if condition_code < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)  # creates a Twilio client
    message = client.messages \
        .create(
        body="It is going to rain today, remember to bring an umbrella ! ",
        from_='+*****',  # here is a Twilio phone number
        to='+*******'  # the phone number to which the message is to be sent
    )
    print(message.status)
