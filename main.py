from extraction.extract_pollution_data import extract_datas
from transformation.transform_pollutions import get_pollutions_data_per_city, get_all_pollutions_data
from loading.load_data import load_pollutions

print(extract_datas())
print(get_pollutions_data_per_city())
print(get_all_pollutions_data())
load_pollutions()