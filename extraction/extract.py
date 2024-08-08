from dotenv import load_dotenv # type: ignore
import os
import requests
import pandas as pd
from utils.convertion import timestamp_to_epoch


#Extract data from OpenWeather
def extract_func(lat, long, city_name):
    load_dotenv()
    api_key = os.getenv('API_KEY')
    url = f'http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={long}&appid={api_key}'

    response = requests.get(url)
    data = response.json()

    aqi_data = data.get('list')[0].get('main') # pick the data for aqi
    poll_data = data.get('list')[0].get('components') #pick data for pollutants
    date_data = data.get('list')[0].get('dt')

    return [aqi_data, poll_data,date_data, city_name]

def extract_local_file(file):
    load_dotenv()
    file_path = os.getenv('FILE_PATH')
    df = pd.read_csv(f'{file_path}/{file}')
    return df

#Extract historical datas from openWeather
def extract_historical(lat, long, city_name, start, end):
    load_dotenv()
    #converting start date and end date to utc
    start_date = timestamp_to_epoch(start)
    end_date = timestamp_to_epoch(end)
    api_key = os.getenv('API_KEY')
    url = f'http://api.openweathermap.org/data/2.5/air_pollution/history?lat={lat}&lon={long}&start={start_date}&end={end_date}&appid={api_key}'

    response = requests.get(url)
    datas = response.json()

    aqis = []
    pollutants = []
    dates = []

    #pick aqi, pollutants and dates 
    for data in datas.get('list'):
        aqis.append(data['main'])
        pollutants.append(data['components'])
        dates.append(data['dt']) 

    return [aqis, pollutants, dates, city_name]