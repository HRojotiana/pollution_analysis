from loading.load_data import manual_load_with_demographic, load_demographic_and_pollutions_in_database, manual_load_with_geographic, load_geographic_and_pollutions_in_database, load_all_datas, manual_load_all_datas
from transformation.transform_pollutions import merge_demographic_and_geographic_datas, merge_all_datas

dates = ['01-08-24' ,'02-08-24' ,'03-08-24', '04-08-24', '05-08-24', '06-08-24','07-08-24','08-08-24']

load_all_datas()

for date in dates:
    manual_load_all_datas(date)