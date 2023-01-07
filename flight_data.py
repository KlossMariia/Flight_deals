import requests


tequilla_url = "https://api.tequila.kiwi.com/locations/query"
tequilla_api = "nfZUDxX6BgliccFiuJlRw8xVeDCacq-1"

# This class find iata codes of different cities using API
class FlightData:
    def __init__(self, city_from, city_to):
        self.cites_list = [city_from, city_to]
        self.iata_codes = []
        self.get_iata_code()

    def get_iata_code(self):
        headers = {
            "apikey": tequilla_api,
        }
        for item in self.cites_list:
            params = {
                "term": item,
                "location_types": "city",
            }
            tequilla_response = requests.get(url=tequilla_url, params=params, headers=headers)
            iata = tequilla_response.json()["locations"][0]["code"]
            self.iata_codes.append(iata)

