from transformation.transform import get_pollutions_city_info_historical, get_all_pollutions_infos
from utils.variables import start_date , end_date 
from utils.coordinates.latitudes import antananarivo_lat, losangeles_lat, lima_lat, nairobi_lat, paris_lat, tokyo_lat 
from utils.coordinates.longitudes import antananarivo_long, losangeles_long, lima_long, nairobi_long, paris_long, tokyo_long

def antananarivo(date):
    return get_pollutions_city_info_historical(antananarivo_lat(), antananarivo_long(), 'Antananarivo', start_date(date), end_date(date))

def losangeles(date):
    return get_pollutions_city_info_historical(losangeles_lat(), losangeles_long(), 'Los Angeles', start_date(date), end_date(date))

def paris(date):
    return get_pollutions_city_info_historical(paris_lat(), paris_long(), 'Paris', start_date(date), end_date(date))

def tokyo(date):
    return get_pollutions_city_info_historical(tokyo_lat(), tokyo_long(), 'Tokyo', start_date(date), end_date(date))

def nairobi(date):
    return get_pollutions_city_info_historical(nairobi_lat(), nairobi_long(), 'Nairobi', start_date(date), end_date(date))

def lima(date):
    return get_pollutions_city_info_historical(lima_lat(), lima_long(), 'Lima', start_date(date), end_date(date))

def all_historical_datas(date):
    lists_of_all = [antananarivo(date), losangeles(date), paris(date), tokyo(date), nairobi(date), lima(date)]
    return get_all_pollutions_infos(lists_of_all)
