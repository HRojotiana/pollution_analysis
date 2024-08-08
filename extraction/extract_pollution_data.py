from extraction.extract import extract_func, extract_historical


def extract_antananarivo_pollution():
    return extract_func(-18.917236014381977, 47.50290091278251, 'Antananarivo')


def extract_losangeles_pollution():
    return extract_func(34.05190409686144, -118.28821070970466, 'Los Angeles')
    

def extract_paris_pollution():
    return extract_func(48.8563407798188, 2.3521811013503524, 'Paris')

def extract_tokyo_pollution():
    return extract_func(35.75209666774653, 139.88399891217742, 'Tokyo')

def extract_nairobi_pollution():
    extract_func(-1.287414704038564, 36.828835485270105, 'Nairobi')

def extract_lima_pollution():
    return extract_func(-12.046591322815443, -77.0537829431234, 'Lima')