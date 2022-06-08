import requests
from datetime import datetime

GENDER = "YOUR_GENDER"
WEIGHT_KG = YOUR_WEIGHT
HEIGHT_CM = YOUR_HEIGHT
AGE = YOUR_AGE

APP_ID = "YOUR_NUTRIONIX_API_ID"
API_KEY = "YOUR_NUTRIONIX_API_KEY"

exercise_text = input("Tell me which exercises you did: ")

nutritionix_api_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = "YOUR_SHEETY_ENDPOINT"

sheety_auth_token = "YOUR_SHEETY_AUTH_TOKEN"

nutritionix_headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

exercise_config = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

sheety_headers = {
    "Authorization": f"Bearer {sheety_auth_token}"
}

response = requests.post(url=nutritionix_api_endpoint, json=exercise_config, headers=nutritionix_headers)
data = response.json()

today = datetime.now()

date = today.strftime('%d/%m/%Y')
time = today.strftime('%H:%M:%S')

for exercise in data["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    sheet_response = requests.post(sheety_endpoint, json=sheet_inputs, headers=sheety_headers)
    print(sheet_response.text)
