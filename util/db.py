import psycopg2
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

def conn():
    print("Trying to make a connection")

    db_database = os.getenv('DB_DATABASE')
    db_host = os.getenv('DB_HOST')
    db_user = os.getenv('DB_USERNAME')
    db_password = os.getenv('DB_PASSWORD')
    db_port = os.getenv('DB_PORT')

    # Make the connection to the database
    connection = psycopg2.connect(database=db_database, user=db_user, password=db_password, host=db_host, port=db_port)
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM accounts.users;")

    record = cursor.fetchall()
    print("Data from Database: - ", record)

    connection.commit()
    connection.close()

# def test():
    