import pandas as pd

class DataProcessor:

    def __init__(self, covid_data):
        self.covid_data = covid_data

    def process_data(self):
        data = self.covid_data.get_overall_data()
        df = pd.DataFrame(data)
        # Process the data using Pandas as needed
        return df

    def process_data_by_country(self, country):
        data = self.covid_data.get_data_by_country(country)
        df = pd.DataFrame(data)
        # Process the data using Pandas as needed
        return df

    def filter_data(self, df, filter_criteria):
        # Filter the data using Pandas based on the provided criteria
        filtered_df = df[df.apply(lambda row: self.check_criteria(row, filter_criteria), axis=1)]
        return filtered_df

    def check_criteria(self, row, filter_criteria):
        # Check if the data row meets the filter criteria
        for key, value in filter_criteria.items():
            if row[key] != value:
                return False
        return True

    def analyze_data(self, df):
        # Analyze the data using Pandas and extract insights
        analysis = {
            "total_cases": df["cases"].sum(),
            "total_deaths": df["deaths"].sum(),
            "total_recoveries": df["recovered"].sum()
        }
        return analysis

    def process_overall_data(self, overall_data):
      processed_data = {
          'TotalConfirmed': overall_data['TotalConfirmed'],
          'TotalDeaths': overall_data['TotalDeaths'],
          'TotalRecovered': overall_data['TotalRecovered'],
          'NewConfirmed': overall_data['NewConfirmed'],
          'NewDeaths': overall_data['NewDeaths'],
          'NewRecovered': overall_data['NewRecovered'],
      }
      return processed_data
