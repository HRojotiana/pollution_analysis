from transformation.transform import get_pollutions_city_info, get_all_pollutions_infos, merge_data_tables
from extraction.extract_local_file import extract_from_demographic_files, extract_from_geographic_file
from transformation.historical_datas_transformation import all_historical_datas
import pandas as pd
from utils.coordinates.latitudes import antananarivo_lat, losangeles_lat, lima_lat, nairobi_lat, paris_lat, tokyo_lat 
from utils.coordinates.longitudes import antananarivo_long, losangeles_long, lima_long, nairobi_long, paris_long, tokyo_long

def get_antananarivo_pollutions_info():
    return get_pollutions_city_info(antananarivo_lat(), antananarivo_long(), 'Antananarivo')

def get_losangeles_pollutions_info():
    return get_pollutions_city_info(losangeles_lat(), losangeles_long(), 'Los Angeles')

def get_paris_pollutions_infos():
    return get_pollutions_city_info(paris_lat(), paris_long(), 'Paris')

def get_tokyo_pollutions_infos():
    return get_pollutions_city_info(tokyo_lat(), tokyo_long(), 'Tokyo')

def get_nairobi_pollutions_info():
    return get_pollutions_city_info(nairobi_lat(), nairobi_long(), 'Nairobi')

def get_lima_pollutions_info():
    return  get_pollutions_city_info(lima_lat(),lima_long(), 'Lima')


def get_pollutions_data_per_city():
    return [get_antananarivo_pollutions_info(), get_losangeles_pollutions_info(), get_paris_pollutions_infos(), get_tokyo_pollutions_infos(), get_nairobi_pollutions_info(), get_lima_pollutions_info()]

def get_all_pollutions_data():
    data_list = get_pollutions_data_per_city()
    return get_all_pollutions_infos(data_list)

def concat_with_historical_datas():
    instant_datas = get_all_pollutions_data()
    historical_datas = all_historical_datas()
    return pd.concat([instant_datas, historical_datas], axis=0)

def merge_with_demographic_datas():
    demographic_datas = extract_from_demographic_files()
    pollutions_datas = concat_with_historical_datas()
    return merge_data_tables(demographic_datas, pollutions_datas)

def merge_with_geographic_datas():
    geographic_datas = extract_from_geographic_file()
    pollutions_datas = concat_with_historical_datas()
    return merge_data_tables(geographic_datas, pollutions_datas)