from transformation.transform import get_pollutions_city_info, get_all_pollutions_infos


def get_pollutions_data_per_city():
    return [get_pollutions_city_info(-18.917236014381977, 47.50290091278251, 'Antananarivo'),
            get_pollutions_city_info(34.05190409686144, -118.28821070970466, 'Los Angeles'),
            get_pollutions_city_info(48.8563407798188, 2.3521811013503524, 'Paris'),
            get_pollutions_city_info(35.75209666774653, 139.88399891217742, 'Tokyo'),
            get_pollutions_city_info(-1.287414704038564, 36.828835485270105, 'Nairobi'),
            get_pollutions_city_info(-12.046591322815443, -77.0537829431234, 'Lima')]


def get_all_pollutions_data():
    data_list = get_pollutions_data_per_city()
    return get_all_pollutions_infos(data_list)
