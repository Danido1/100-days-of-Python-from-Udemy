import requests
from flight_data import FlightData


TEQUILA_APIKEY = "LrxPv_ySr75C08XhFjATeJIvoi3-h-k0"
TEQUILA_GET = "https://tequila-api.kiwi.com/locations/query"
SEARCH_API = "https://tequila-api.kiwi.com/v2/search"


class FlightSearch:

    def get_iat_code(self, city_name):
        headers = {"apikey": TEQUILA_APIKEY}
        my_params = {"term": city_name, "location_types": "city"}
        response = requests.get(url=TEQUILA_GET, headers=headers, params=my_params)
        results = response.json()["locations"]
        code = results[0]["code"]
        return code

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):

        headers = {"apikey": TEQUILA_APIKEY}
        query = {
            "fly:from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP"
            }
        response = requests.get(
                url=SEARCH_API,
                headers=headers,
                params=query
            )

        print(response.json())

        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {destination_city_code}.")
            return None

        flight_data = FlightData(
            max_price=data["price"],
            fly_from_city=data["route"][0]["cityFrom"],
            fly_from_airport=data["route"][0]["flyFrom"],
            fly_to_city=data["route"][0]["cityTo"],
            fly_to_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]

        )

        print(f"{flight_data.fly_to_city}: £{flight_data.max_price}")
        return flight_data
