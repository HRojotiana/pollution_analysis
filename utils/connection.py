import psycopg2
from dotenv import load_dotenv
from sqlalchemy import create_engine
import os 
import sys

def db_connect():
    """Connect to database"""
    load_dotenv()
    connection_url = os.getenv('DB_URL')
    engine = create_engine(connection_url)
    return engine