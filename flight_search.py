import requests
from flight_data import FlightData
from pprint import pprint

TEQUILA_API_ENDPOINT = "https://tequila-api.kiwi.com/v2/search"
TEQUILA_API_KEY = "YOUR_TEQUILA_API_KEY"

header = {
    "apiKey": TEQUILA_API_KEY
}


class FlightSearch:
    def get_destination_code(self, city_name):
        query = {"term": city_name, "location_types": "city"}
        response = requests.get(url="https://tequila-api.kiwi.com/locations/query", headers=header, params=query)
        data = response.json()
        code = data["locations"][0]["code"]
        return code

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        flight_params = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "dateFrom": from_time,
            "dateTo": to_time,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "INR",
        }

        response = requests.get(url=TEQUILA_API_ENDPOINT, headers=header, params=flight_params)
        try:
            data = response.json()["data"][0]
        except IndexError:
            flight_params["max_stopovers"] = 1
            response = requests.get(url=TEQUILA_API_ENDPOINT, headers=header, params=flight_params)
            try:
                data = response.json()["data"][0]
            except IndexError:
                return None
            else:
                pprint(data)
                flight_data = FlightData(
                    price=data["price"],
                    origin_city=data["route"][0]["cityFrom"],
                    origin_airport=data["route"][0]["flyFrom"],
                    destination_city=data["route"][1]["cityTo"],
                    destination_airport=data["route"][1]["flyTo"],
                    out_date='/'.join(data["route"][0]["local_departure"].split('T')[0].split('-')[::-1]),
                    return_date='/'.join(data["route"][2]["local_departure"].split('T')[0].split('-')[::-1]),
                    stop_overs=1,
                    via_city=data["route"][0]["cityTo"]
                )
                return flight_data
        else:
            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][0]["cityTo"],
                destination_airport=data["route"][0]["flyTo"],
                out_date='/'.join(data["route"][0]["local_departure"].split('T')[0].split('-')[::-1]),
                return_date='/'.join(data["route"][1]["local_departure"].split('T')[0].split('-')[::-1])
            )
            return flight_data
