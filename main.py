from extraction.extract_pollution_data import extract_geographic_pollution, extract_demographic_pollution
from transformation.transform import remove_duplicated_lines
from loading.load_data import load_demographic_and_pollutions_in_database

df = extract_demographic_pollution()
print(df.duplicated())
print(f"Duplicated values number : {df.duplicated().sum()}")
no_duplicates = remove_duplicated_lines(df)
print(no_duplicates)
print(f"Duplicated values number : {no_duplicates.duplicated().sum()}")

# load_demographic_and_pollutions_in_database()