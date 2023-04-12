import requests

class CovidData:

    def __init__(self, api_url):
        self.api_url = "https://covid19api.herokuapp.com"
        self.data = None

    def fetch_data(self):
        response = requests.get(self.api_url)
        if response.status_code == 200:
            self.data = response.json()
        else:
            print("Error fetching data:", response.status_code)

    def fetch_data_by_country(self, country):
        response = requests.get(f"{self.base_url}/countries/{country}")
        if response.status_code == 200:
            self.data = response.json()
        else:
            print("Error fetching data:", response.status_code)