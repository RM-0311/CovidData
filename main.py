from covid_data import CovidData
from data_processor import DataProcessor
from data_visualizer import DataVisualizer

def main():
    # Instantiate the classes
    covid_data = CovidData()
    data_processor = DataProcessor(covid_data)
    data_visualizer = DataVisualizer(data_processor)

    # Fetch the data using the CovidData class
    overall_data = covid_data.fetch_overall_data()
    country_data = covid_data.fetch_data_by_country('USA')  # Replace 'USA' with the desired country

    # Process the data using the DataProcessor class
    processed_overall_data = data_processor.process_overall_data(overall_data[0])
    print(country_data)
    processed_country_data = data_processor.process_country_data(country_data)

    # Visualize the data using the DataVisualizer class
    data_visualizer.plot_overall_data(processed_overall_data)
    data_visualizer.plot_country_data(processed_country_data)

if __name__ == "__main__":
    main()
