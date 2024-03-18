import requests
from pprint import pprint
from data_manager import DataManager
from flight_search import FlightSearch
import datetime

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()

SHEETY_POST = "https://api.sheety.co/e6e5f54934a6b656b5cf102b2ed6a7db/flightDeals/prices"
SHEETY_PUT = "https://api.sheety.co/e6e5f54934a6b656b5cf102b2ed6a7db/flightDeals/prices/[Object ID]"

if (sheet_data[0]['iataCode']) == "":
    from flight_search import FlightSearch
    fligh_search = FlightSearch()
    for row in sheet_data:
        row['iataCode'] = fligh_search.get_iat_code(row["city"])
        print(f"sheet_data:\n {sheet_data}")

CURRENT_DATE = datetime.datetime.now()
DATE_IN_SIX_MONTHS = datetime.datetime.now() + datetime.timedelta(minutes=262800)  # 6 months in minutes

for destination in sheet_data:
    flight = flight_search.check_flights(
        "LON",
        destination["iataCode"],
            from_time=CURRENT_DATE,
        to_time=DATE_IN_SIX_MONTHS

    )


data_manager.destination_data = sheet_data
data_manager.update_destination_codes()