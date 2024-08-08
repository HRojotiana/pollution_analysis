from transformation.historical_datas_transformation import antananarivo, all_historical_datas
from utils.coordinates.latitudes import antananarivo_lat, losangeles_lat, lima_lat, nairobi_lat, paris_lat, tokyo_lat 
from transformation.transform_pollutions import concat_with_historical_datas, get_all_pollutions_data
from loading.load_data import load_geographic_and_pollutions_in_database, load_demographic_and_pollutions_in_database

# print(concat_with_historical_datas())
print(get_all_pollutions_data())
