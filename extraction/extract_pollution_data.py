from extraction.extract import extract_func, extract_from_database
from utils.coordinates.latitudes import antananarivo_lat, losangeles_lat, lima_lat, nairobi_lat, paris_lat, tokyo_lat 
from utils.coordinates.longitudes import antananarivo_long, losangeles_long, lima_long, nairobi_long, paris_long, tokyo_long


def extract_antananarivo_pollution():
    return extract_func(antananarivo_lat(), antananarivo_long(), 'Antananarivo')


def extract_losangeles_pollution():
    return extract_func(losangeles_lat(), losangeles_long(), 'Los Angeles')
    

def extract_paris_pollution():
    return extract_func(paris_lat(), paris_long(), 'Paris')

def extract_tokyo_pollution():
    return extract_func(tokyo_lat(), tokyo_long(), 'Tokyo')

def extract_nairobi_pollution():
    extract_func(nairobi_lat(), nairobi_long(), 'Nairobi')

def extract_lima_pollution():
    return extract_func(lima_lat(), lima_long(), 'Lima')

def extract_demographic_pollution():
    return extract_from_database('demographic_pollution_datas')

def extract_geographic_pollution():
    return extract_from_database('geographic_pollution_datas')

def aqis_datas():
    return extract_from_database('aqis')