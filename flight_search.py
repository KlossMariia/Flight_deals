import requests
from data_manager import DataManager
import json

tequilla_api = "nfZUDxX6BgliccFiuJlRw8xVeDCacq-1"
tequilla_url = "https://api.tequila.kiwi.com/search"

# This class searches for flights information
# It gets needed data from GUI interface
class FlightSearch:

    def __init__(self, iata_codes, date:str, max_stopovers:int):
        self.date = date
        # iata codes from FlightData are used for flights searching
        self.iata_codes = iata_codes
        self.max_stopovers = max_stopovers
        self.response = self.flight_search()

        DataManager(self.response) # sends information for writing it to excel

    def flight_search(self):
        headers = {
            "apikey": tequilla_api,
        }
        params = {
            "fly_to": self.iata_codes[1],
            "fly_from": self.iata_codes[0],
            "date_from": self.date,
            "date_to": self.date,
            "max_stopovers": self.max_stopovers,
            "curr": "EUR",
        }
        response = requests.get(url=tequilla_url, headers=headers, params=params)
        result = json.loads(response.text) # converts str to json
        return result



