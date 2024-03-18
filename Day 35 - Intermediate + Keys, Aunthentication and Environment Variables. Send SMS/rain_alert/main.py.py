import requests
from twilio.rest import Client
import os
my_api_key = "51a804f46da4e11d7e5e189456e465e4"
angela_api_key = os.environ.get("OWN_API_KEY")

# Twilio details
account_sid = os.environ.get("identification") #Identification for Twilio account
auth_token = os.environ.get("OWN_AUTH_TOKEN")


MY_LAT = 40.396129
MY_LON = -3.608713
OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"


parameters = {
    "lat": MY_LAT,
    "lon": MY_LON,
    "appid": angela_api_key,
    "exclude": "current,minutely,daily",
    "units": "imperial"
}

response = requests.get(OWM_ENDPOINT, params=parameters)
response.raise_for_status()
weather_data = response.json()
print(weather_data)
#print((weather_data)["hourly"][0])
#print((weather_data)["hourly"][0]["weather"])
#weather_condition_first_hour = print((weather_data)["hourly"][hour]["weather"][0]["id"])
#print(weather_condition_first_hour)

will_rain = False

for hour in range(12):
    weather_condition = ((weather_data)["hourly"][hour]["weather"][0]["id"])
    print(f"{hour}:{weather_condition}")
    if int(weather_condition) < 700:
        will_rain = True


if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body='☔Llevate un paraguas que va a llover☔',
        to='whatsapp:+myphone'
    )


    print(message.sid)




