import pandas as pd
from dotenv import load_dotenv 
import os
import psycopg2  
from sqlalchemy import create_engine 
import time
from utils.connection import db_connect


def save_to_csv_format(df, file_name):
    df.to_csv(f"{file_name}.csv", index=False)
    print(f'{file_name} created in csv format')

def load_to_database(df, table_name):
    engine = db_connect()
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