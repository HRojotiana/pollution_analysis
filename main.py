from transformation.transform_pollutions import merge_with_demographic_datas, merge_with_geographic_datas
from transformation.transform import get_all_pollutions_infos
from extraction.extract_local_file import extract_from_demographic_files
from loading.load_data import load_demographic_and_pollutions

print(merge_with_geographic_datas())
print(type(merge_with_demographic_datas()))
load_demographic_and_pollutions()