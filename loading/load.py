import pandas as pd


def save_to_csv_format(df, file_name):
    df.to_csv(f"{file_name}.csv", index=False)
    print(f'{file_name} created in csv format')
