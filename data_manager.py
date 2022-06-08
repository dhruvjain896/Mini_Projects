import requests

API_ENDPOINT = "YOUR_SHEETY_API_ENDPOINT"


class DataManager:
    def __init__(self):
        self.destination_data = {}

    def get_data(self):
        response = requests.get(API_ENDPOINT)
        data = response.json()
        self.destination_data = data['prices']
        return self.destination_data

    def put_data(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(f"{API_ENDPOINT}/{city['id']}", json=new_data)
