from covid_data import CovidData
from data_processor import DataProcessor
from data_visualizer import DataVisualizer

def main():
    # Instantiate the classes
    covid_data = CovidData()
    data_processor = DataProcessor(covid_data)
    data_visualizer = DataVisualizer(data_processor)

    # STATIC DATA - API IS DOWN
    overall_data = {
        "TotalConfirmed": 100000,
        "TotalDeaths": 2000,
        "TotalRecovered": 95000,
        "NewConfirmed": 100,  
        "NewDeaths": 10,
        "NewRecovered": 90
    }
    country_data = [
        {
            "Country": "United States",
            "Cases": 1000,
            "Date": "2023-01-01T00:00:00Z",
        },
        {
            "Country": "United States",
            "Cases": 2000,
            "Date": "2023-01-02T00:00:00Z",
        },
        {
            "Country": "United States",
            "Cases": 3000,
            "Date": "2023-01-03T00:00:00Z",
        },
    ]
    # Process the data using the DataProcessor class
    processed_overall_data = data_processor.process_overall_data(overall_data)
    processed_country_data = data_processor.process_country_data(country_data)

    # Visualize the data using the DataVisualizer class
    data_visualizer.plot_overall_data(processed_overall_data)
    data_visualizer.plot_country_data(processed_country_data)

if __name__ == "__main__":
    main()
