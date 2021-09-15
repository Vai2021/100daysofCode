import requests
from pprint import pprint

SHEET_ENDPOINT = "https://api.sheety.co/f4d7e983d026f93f5aa68daed721d762/flightDeals/prices"


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEET_ENDPOINT)
        data = response.json()
        self.destination_data = data["prices"]
        # pprint(data)
        return self.destination_data

    # update destination code IATA codes
    def update_destination_code(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(url=f"{SHEET_ENDPOINT}/{city['id']}", json=new_data)
            print(response.text)
