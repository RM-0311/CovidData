import matplotlib.pyplot as plt

class DataVisualizer:
    def __init__(self, data_processor):
        self.data_processor = data_processor

    def plot_cases_by_country(self, countries, days=30):
        for country in countries:
            country_data = self.data_processor.get_country_data(country)
            if country_data is not None:
                dates = country_data["date"][-days:]
                cases = country_data["cases"][-days:]
                plt.plot(dates, cases, label=country)

        plt.xlabel("Date")
        plt.ylabel("Cases")
        plt.title("COVID-19 Cases by Country")
        plt.legend()
        plt.show()

    # Add more visualization methods as needed
