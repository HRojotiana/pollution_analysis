from extraction.extract import extract_local_file

def extract_from_demographic_files():
    return (extract_local_file('Demographic_Data.csv'))


def extract_from_geographic_file():
    return (extract_local_file('Geographic_Data.csv'))