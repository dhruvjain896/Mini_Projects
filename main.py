import requests
from datetime import datetime
import smtplib
import time

my_email = "youremailid@gmail.com"
password = "password"

MY_LAT = 29.910999  # Your latitude
MY_LONG = 77.539017  # Your longitude


def iss_overhead_checker():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_longitude = float(data["iss_position"]["longitude"])
    iss_latitude = float(data["iss_position"]["latitude"])

    # Your position is within +5 or -5 degrees of the ISS position.
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True
    return False


def night_time_checker():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0
    }
    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(':')[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(':')[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True
    return False


while True:
    time.sleep(60)
    if iss_overhead_checker() and night_time_checker():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs="youremailid@gmail.com",
                msg=f"Subject:Look Up\n\nThe ISS is above you in the sky."
            )
