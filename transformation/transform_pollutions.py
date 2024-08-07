from transformation.transform import get_pollutions_city_info, get_all_pollutions_infos, merge_data_tables
from extraction.extract_local_file import extract_from_demographic_files, extract_from_geographic_file


def get_antananarivo_pollutions_info():
    return get_pollutions_city_info(-18.917236014381977, 47.50290091278251, 'Antananarivo')

def get_losangeles_pollutions_info():
    return get_pollutions_city_info(34.05190409686144, -118.28821070970466, 'Los Angeles')

def get_paris_pollutions_infos():
    return get_pollutions_city_info(48.8563407798188, 2.3521811013503524, 'Paris')

def get_tokyo_pollutions_infos():
    return get_pollutions_city_info(35.75209666774653, 139.88399891217742, 'Tokyo')

def get_nairobi_pollutions_info():
    return get_pollutions_city_info(-1.287414704038564, 36.828835485270105, 'Nairobi')

def get_lima_pollutions_info():
    return  get_pollutions_city_info(-12.046591322815443, -77.0537829431234, 'Lima')


def get_pollutions_data_per_city():
    return [get_antananarivo_pollutions_info(), get_losangeles_pollutions_info(), get_paris_pollutions_infos(), get_tokyo_pollutions_infos(), get_nairobi_pollutions_info(), get_lima_pollutions_info()]

def get_all_pollutions_data():
    data_list = get_pollutions_data_per_city()
    return get_all_pollutions_infos(data_list)

def merge_with_demographic_datas():
    demographic_datas = extract_from_demographic_files()
    pollutions_datas = get_all_pollutions_data()
    return merge_data_tables(demographic_datas, pollutions_datas)

def merge_with_geographic_datas():
    geographic_datas = extract_from_geographic_file()
    pollutions_datas = get_all_pollutions_data()
    return merge_data_tables(geographic_datas, pollutions_datas)