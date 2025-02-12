import psycopg2
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

def insertDatabase(name):
    # Retrieve database information from .env file
    db_database = os.getenv('DB_DATABASE')
    db_host = os.getenv('DB_HOST')
    db_user = os.getenv('DB_USERNAME')
    db_password = os.getenv('DB_PASSWORD')
    db_port = os.getenv('DB_PORT')

    try:
        # Make the connection to the database
        connection = psycopg2.connect(database=db_database, user=db_user, password=db_password, host=db_host, port=db_port)
    except Exception as error:
        print('Failed to Connect')
        print(error)
  
    cursor = connection.cursor()

    try:
        # Insert into the database
        cursor.execute("INSERT INTO organizations.entries(name) VALUES (%s)", (name,))
        print('Successfully insert into organizations')
    except Exception as error:
        print('Failed to insert into database')
        print(error)

    # Commit the change
    connection.commit()
    # Close the connection
    connection.close()
