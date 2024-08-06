from loading.load import save_to_csv_format
from transformation.transform_pollutions import get_pollutions_data_per_city,get_all_pollutions_infos, merge_with_geographic_datas, merge_with_demographic_datas


def load_pollutions():
    data_list = get_all_pollutions_infos()
    return save_to_csv_format(data_list, 'pollutions')

def load_demographic_and_pollutions():
    data_list = merge_with_demographic_datas()
    return save_to_csv_format(data_list, 'pollutions_and_demographic')
def load_geographic_and_pollutions():
    data_list = merge_with_geographic_datas()
    return save_to_csv_format(data_list, 'pollutions_and_demographic')