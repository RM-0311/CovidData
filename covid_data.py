import requests

class CovidData:

    def __init__(self):
        self.base_url = "https://covid19api.herokuapp.com"
        self.data = None

    def fetch_data(self):
        response = requests.get(f"{self.base_url}/all")
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

    def fetch_overall_data(self):
        # Fetch overall data
        url = "https://api.covid19api.com/world"
        response = requests.get(url)
        data = response.json()
        return data
