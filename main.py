import requests
from twilio.rest import Client
import os

api_key = os.getenv('YOUR_API_KEY')
account_sid = os.getenv('YOUR_ACCOUNT_SID')
auth_token = os.getenv('YOUR_AUTH_TOKEN')
mobile_number = os.getenv('YOUR_NUMBER')
twilio_mobile_number = os.getenv('YOUR_TWILIO_NUMBER')
twilio_whatsapp_number = os.getenv('YOUR_TWILIO_WHATSAPP_NUMBER')

# Use your latitude and longitude
LAT = 29.963659
LON = 77.546028


parameters = {
    "lat": LAT,
    "lon": LON,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

api = "https://api.openweathermap.org/data/2.5/onecall"

response = requests.get(api, params=parameters)
response.raise_for_status()
weather_data = response.json()

hourly_weather = [n["weather"][0]["id"] for n in weather_data["hourly"][:12]]

will_rain = False

for i in hourly_weather:
    if i < 700:
        will_rain = True
        break

# For SMS
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an ☔",
        from_=f"{twilio_mobile_number}",
        to=f"{mobile_number}"
    )
    print(message.sid)

# For Whatsapp
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☔",
        from_=f"whatsapp:{twilio_whatsapp_number}",
        to=f"whatsapp:{mobile_number}"
    )
    print(message.status)
