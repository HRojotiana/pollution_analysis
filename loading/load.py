from transformation.transform import get_all_pollutions_infos


def save_to_csv_format(all_infos, file_name):
    df = get_all_pollutions_infos(all_infos)
    df.to_csv(f"{file_name}.csv", index=False)
    print(f'{file_name} created in csv format')
