from extraction.extract import extract_local_file

def extract_from_files():
    return (extract_local_file('Demographic_Data.csv'), extract_local_file('Geographic_Data.csv'))

