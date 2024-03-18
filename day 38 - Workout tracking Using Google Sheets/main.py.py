# python datetime strftime(), apis and making post requests. authorization headers, environment variables
import requests
from datetime import datetime
from requests.auth import HTTPBasicAuth
import os

# BASIC AUTHENTICATOR
basic = HTTPBasicAuth('test', 'test123')


END_POINT_NUTRITIONIX = "https://trackapi.nutritionix.com/v2/natural/exercise"
ENDPOINT_POST_SHEETY = "https://api.sheety.co/e6e5f54934a6b656b5cf102b2ed6a7db/workoutTracking/workouts"

#API_ID = "8083dbf0"
API_ID = os.environ["API_ID"]
#API_KEY = "c2186ddd13ff7e4cc8ff2421b5eb5ae7"
API_KEY = os.environ["API_KEY"]

QUESTION = input("What exercise you did?: ")



headers = {
    "x-app-id": API_ID,
    "x-app-key": API_KEY,
}

params = {
    "query": QUESTION,
    "gender": "male",
    "weight_kg": 75,
    "height_cm": 1.73,
    "age": 27,
}

response = requests.post(url=END_POINT_NUTRITIONIX, json=params, headers=headers)
result = response.json()
print(result)
print(result["exercises"][0]["tag_id"])
today = datetime.now()
now_time = datetime.now().strftime("%X")

exercirse_params = {
    "workout": {
        "date": today.strftime("%d/%m/%y"),
        "time": now_time,
        "exercise": (result["exercises"][0]["user_input"]).title(),
        "duration": (result["exercises"][0]["duration_min"]),
        "calories": (result["exercises"][0]["nf_calories"])
    }
}

sheet_response = requests.post(url=ENDPOINT_POST_SHEETY, json=exercirse_params, auth=basic)
print(sheet_response.text)