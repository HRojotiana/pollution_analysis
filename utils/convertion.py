import pandas as pd

def timestamp_to_epoch(date):
    timestamp = pd.to_datetime(date, format='%d-%m-%y %H:%M:%S')

    epoch_time = int(timestamp.timestamp())
    return epoch_time