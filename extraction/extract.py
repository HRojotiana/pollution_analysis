import os
import requests


#Extract data from OpenWeather
def extract_func(lat, long, city_name):
    api_key = os.getenv('API_KEY')
    url = f'http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={long}&appid={api_key}'

    response = requests.get(url)
    data = response.json()

    aqi_data = data.get('list')[0].get('main') #pick the data for aqi
    poll_data = data.get('list')[0].get('components') #pick data for pollutants

    return [aqi_data, poll_data, city_name]