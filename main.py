from covid_data import CovidData
from data_processor import DataProcessor
from data_visualizer import DataVisualizer

# Initialize and fetch data
covid_data = CovidData(api_url='https://covid19api.herokuapp.com')
covid_data.fetch_data()

# Process and analyze data
data_processor = DataProcessor(covid_data.data)
# Call methods to process and analyze data

# Create visualizations
data_visualizer = DataVisualizer(data_processor.data)
# Call methods to create visualizations
