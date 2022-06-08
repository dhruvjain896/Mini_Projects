from data_manager import DataManager
from flight_search import FlightSearch
from datetime import datetime, timedelta
from notification_manager import NotificationManager
import requests

sheety_user_api_endpoint = "YOUR_SHEETY_API_ENDPOINT"


def acquire_customer():
    print("Welcome to Dhruv's Flight Club.")
    print("We find the best flight deals and email you.")
    first_name = input("What is you first name?\n")
    last_name = input("What is your last name?\n")
    email = input("What is your email?\n")
    confirm_email = input("Type your email again.\n")

    if email == confirm_email:
        print("Success your email has been added, You're in the club!")

        new_data = {
            "user": {
                "firstName": first_name,
                "lastName": last_name,
                "email": email
            }
        }

        response = requests.post(url=sheety_user_api_endpoint, json=new_data)


# acquire_customer()

today_date = datetime.now().strftime('%d/%m/%Y')
six_months_later = (datetime.strptime(today_date, "%d/%m/%Y") + timedelta(days=181)).strftime('%d/%m/%Y')

sheety = DataManager()
sheet_data = sheety.get_data()
flight_search = FlightSearch()
notification = NotificationManager()

ORIGIN_CITY_IATA = "DEL" #CHANGE IT TO YOUR CITY'S IATA CODE

if sheet_data[0]["iataCode"] == "":
    for i in sheet_data:
        i["iataCode"] = flight_search.get_destination_code(i["city"])

    sheety.destination_data = sheet_data
    sheety.put_data()

for destination in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=today_date,
        to_time=six_months_later,
    )

    if flight is None:
        continue

    if flight.price < destination["lowestPrice"]:
        message = f"Low price alert! Only Rs{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
        if flight.stop_overs > 0:
            message += f"\nFlight has {flight.stop_overs} stop over, via {flight.via_city}."
        # notification.send_whatsapp(message)
        notification.send_email(message)
