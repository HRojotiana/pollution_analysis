from transformation.transform import get_all_pollutions_infos
import pandas as pd


def save_to_csv_format(all_infos, file_name):
    df = get_all_pollutions_infos(all_infos)
    date = pd.Timestamp.now()
    df.to_csv(f"{file_name}_{date}.csv", index=False)
    print(f'{file_name} created in csv format')
