from loading.load import save_to_csv_format, load_to_database, load_to_database_replace
from transformation.transform_pollutions import get_all_pollutions_infos, merge_with_geographic_datas, merge_with_demographic_datas, hist_merge_with_demographic_datas, hist_merge_with_geographic_datas, merge_all_datas, hist_merge_all_datas, aqi_info_per_location


def load_pollutions():
    data_list = get_all_pollutions_infos()
    return save_to_csv_format(data_list, 'pollutions')

def load_demographic_and_pollutions():
    data_list = merge_with_demographic_datas()
    return save_to_csv_format(data_list, 'pollutions_and_demographic')

def load_geographic_and_pollutions():
    data_list = merge_with_geographic_datas()
    return save_to_csv_format(data_list, 'pollutions_and_demographic')

def load_demographic_and_pollutions_in_database():
    data_list = merge_with_demographic_datas()
    load_to_database(data_list, 'demographic_pollution_datas')

def load_geographic_and_pollutions_in_database():
    data_list = merge_with_geographic_datas()
    load_to_database(data_list, 'geographic_pollution_datas')

def load_all_datas():
    data_list = merge_all_datas()
    load_to_database(data_list, 'pollutions')

#Load manually historical datas
def manual_load_with_demographic(date):
    data_list = hist_merge_with_demographic_datas(date)
    load_to_database(data_list, 'demographic_pollution_datas')

def manual_load_with_geographic(date):
    data_list = hist_merge_with_geographic_datas(date)
    load_to_database(data_list, 'geographic_pollution_datas')

def manual_load_all_datas(date):
    data_list = hist_merge_all_datas(date)
    load_to_database(data_list, 'air_pollutions')

#Load aqi informations per location*
def aqi_per_location():
    data_list = aqi_info_per_location()
    load_to_database_replace(data_list, "aqis")