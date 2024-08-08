from transformation.transform import get_pollutions_city_info_historical, get_all_pollutions_infos
from utils.variables import start_date , end_date 
from utils.coordinates.latitudes import antananarivo_lat, losangeles_lat, lima_lat, nairobi_lat, paris_lat, tokyo_lat 
from utils.coordinates.longitudes import antananarivo_long, losangeles_long, lima_long, nairobi_long, paris_long, tokyo_long

def antananarivo():
    return get_pollutions_city_info_historical(antananarivo_lat(), antananarivo_long(), 'Antananarivo', start_date(), end_date())

def losangeles():
    return get_pollutions_city_info_historical(losangeles_lat(), losangeles_long(), 'Los Angeles', start_date(), end_date())

def paris():
    return get_pollutions_city_info_historical(paris_lat(), paris_long(), 'Paris', start_date(), end_date())

def tokyo():
    return get_pollutions_city_info_historical(tokyo_lat(), tokyo_long(), 'Tokyo', start_date(), end_date())

def nairobi():
    return get_pollutions_city_info_historical(nairobi_lat(), nairobi_long(), 'Nairobi', start_date(), end_date())

def lima():
    return get_pollutions_city_info_historical(lima_lat(), lima_long(), 'Lima', start_date(), end_date())

def all_historical_datas():
    lists_of_all = [antananarivo(), losangeles(), paris(), tokyo(), nairobi(), lima()]
    return get_all_pollutions_infos(lists_of_all)
