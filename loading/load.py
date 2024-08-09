import pandas as pd
from dotenv import load_dotenv 
import os
import psycopg2  
from sqlalchemy import create_engine 
import time


def save_to_csv_format(df, file_name):
    df.to_csv(f"{file_name}.csv", index=False)
    print(f'{file_name} created in csv format')

def load_to_database(df, table_name):
    load_dotenv()
    connection_url = os.getenv('DB_URL')
    engine = create_engine(connection_url)
    start_time = time.time()

    df.to_sql(
        name=table_name,
        con=engine,
        if_exists="append",
        index=False
    )

    end_time = time.time()
    total_time = end_time - start_time
    print(f'Insert time: {total_time} seconds')