from loading.load import save_to_csv_format
from transformation.transform_pollutions import get_pollutions_data_per_city


def load_pollutions():
    data_list = get_pollutions_data_per_city()
    return save_to_csv_format(data_list, 'pollutions')