import requests

SHEETY_GET = "https://api.sheety.co/e6e5f54934a6b656b5cf102b2ed6a7db/flightDeals/prices"
SHEETY_PUT = "https://api.sheety.co/e6e5f54934a6b656b5cf102b2ed6a7db/flightDeals/prices"


class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_GET)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                    "price": {
                        "iataCode": city["iataCode"]
            }
            }
            r = requests.put(
                url=f"{SHEETY_PUT}/{city['id']}",
                json=new_data)
            print(r.text)


