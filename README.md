# Rain-Alert
Python app made with the Twilio API that sends a SMS to a phone number if rain will fall during the day.

This app will alert the user via SMS if it is raining during the day.

First, we need to make a GET request to the Open Weather Map One Call API. I use my API key for this and I provide the geographical coordinates of my location,
as parameters fro my request. I also exclude from the potential reponse the current, daily and monthly data. I only want to get the hourly weather data for 
the day.

Once, we get a reponse we parse the JSON data we get back. Then we are gong to tap into the data we just parsed and try to retrieve the 12 weather codes
for the first 12 hours of the day. Basically, the Open Weather Map API associate to each weather condition a three digits code (under the key "weather" 
and then "id"). 

Read the documentation for the One Call API of the OPen Weather Map for more info here : https://openweathermap.org/api/one-call-api

Any code below 700 is synonymous with rain, snow or drizzle. As a result if one of these twelve weather codes fall below 700, 
we can send an SMS to the user.

To send an SMS to the user, we must create a Twilio account and obtain our credentials (account SID and auth token). Using these credentials,
we can send a message to the user using the Twilio. We just need to provide a body of text for the message to send as well as a phone number
from which the message is sent (provided by Twilio) and a phone number to which the message is to be sent (the user's personal phone number for example).

To test the program, we can modify the location coordinates (latitude and longitude) to a location on Earth where it is raining and the program will send indeed
an SMS with the text written under the message parameter.




