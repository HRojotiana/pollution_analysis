import pandas as pd
import numpy as np
from extraction.extract import extract_func, extract_historical


def convert_to_df(lat, long, city):
    datas = extract_func(lat, long, city)
    aqi = []
    pollutants = []
    date = []

    for x in range(1):
        aqi.append(datas[0])
        pollutants.append(datas[1])
        date.append(datas[2])

    aqi_df = pd.DataFrame.from_dict(aqi)
    pollutants_df = pd.DataFrame.from_dict(pollutants)
    date_df = pd.DataFrame.from_dict(date)
    return [aqi_df, pollutants_df, date_df, city]

def convert_historical_to_df(lat, long, city, start, end):
    datas = extract_historical(lat, long, city, start, end)

    aqi_df = pd.DataFrame.from_dict(datas[0])
    pollutants_df = pd.DataFrame.from_dict(datas[1])
    dates_df = pd.DataFrame.from_dict(datas[2])

    return[aqi_df, pollutants_df, dates_df, city]

def get_pollutions_city_info(lat, long, location):
    dfs = convert_to_df(lat, long, location)
    df = pd.concat([dfs[0], dfs[1], dfs[2]], axis=1)
    df['Location'] = location
    df.rename(columns={0:'Date'}, inplace=True)
    df['Date'] = pd.to_datetime(df['Date'], unit='s') 

    return df

def get_pollutions_city_info_historical(lat, long, location, start, end):
    dfs = convert_historical_to_df(lat, long, location, start, end)
    df = pd.concat([dfs[0], dfs[1], dfs[2]], axis=1)
    df['Location'] = location
    df.rename(columns={0:'Date'}, inplace=True)
    df['Date'] = pd.to_datetime(df['Date'], unit='s') 

    return df

#all_infos: arrays of all cities datas
def get_all_pollutions_infos(all_infos):
    df = pd.concat(all_infos, axis=0, ignore_index=True)
    return df

#Merge pollution datas to other datas information about cities
def merge_data_tables(datas_to_be_merged, pollution_datas):
    return pd.merge(pollution_datas, datas_to_be_merged, how='inner', on=["Location"])

#Removing duplicated values
