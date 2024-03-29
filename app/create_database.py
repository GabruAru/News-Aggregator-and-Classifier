import psycopg2
from dotenv import load_dotenv
from psycopg2 import OperationalError ,ProgrammingError
import logging 
import os

load_dotenv()

username = os.environ['user']
password = os.environ['password']
database_name = os.environ['Database_Name']


def create_database():
    logging.info("Database creation in progress....")
    try:
        connection = psycopg2.connect(
            user=username,
            password=password,
            host="localhost",
            port="5432",
        )

        cursor = connection.cursor()

        connection.autocommit = True 
        cursor.execute(f"CREATE DATABASE {database_name}")
        connection.commit()
        logging.info("Database created successfully")
        
    except ProgrammingError as e:
        logging.info(f"The database '{database_name}' already exists")
    except OperationalError as e:
        logging.info(f"The error '{e}' occurred")
        
    finally:
        
        if connection:
            cursor.close()
            connection.close()
            logging.info("Connection closed")


