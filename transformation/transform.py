import pandas as pd
import numpy as np
from extraction.extract import extract_func
import datetime


def convert_to_df(lat, long, city):
    datas = extract_func(lat, long, city)
    aqi = []
    pollutants = []

    for x in range(1):
        aqi.append(datas[0])
        pollutants.append(datas[1])

    aqi_df = pd.DataFrame.from_dict(aqi)
    pollutants_df = pd.DataFrame.from_dict(pollutants)
    return [aqi_df, pollutants_df, city]

def get_pollutions_city_info(lat, long, location):
    dfs = convert_to_df(lat, long, location)
    df = pd.concat([dfs[0], dfs[1]], axis=1)
    df['Location'] = location
    df['Date'] = pd.Timestamp.now().date()

    return df


def get_all_pollutions_infos(all_infos):
    df = pd.concat(all_infos, axis=0, ignore_index=True)
    return df

def merge_data_tables(datas_to_be_merged, pollution_datas):
    return pd.merge(pollution_datas, datas_to_be_merged, how='inner', on=["Location"])