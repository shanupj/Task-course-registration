import os
import mysql.connector
import pandas as pd
from mysql.connector import Error

# Load environment variables for database credentials
DB_HOST = os.getenv('DB_HOST')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_NAME = os.getenv('DB_NAME')

def fetch_course_registration_data():
    connection = None  # Connection is initialised to None
    try:
        # Establish database connection using environment variables
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='root',
            database='courseRegistration'
        )

        if connection.is_connected():
            print("Connected to the database")

            # SQL query to fetch the data
            query = """
            SELECT Account.program AS Program, 
                   Account.email AS Email, 
                   Course.name AS Course_name, 
                   TermCourseRegistrationApplication.applying_level AS Applying_level, 
                   Account.current_level AS Current_level, 
                   Course.fee AS Fee_details, 
                   Application.status AS Application_status 
            FROM TermCourseRegistrationApplication 
            JOIN Application ON TermCourseRegistrationApplication.application_id = Application.id 
            JOIN Account ON Application.account_id = Account.id 
            JOIN Course ON TermCourseRegistrationApplication.course_id = Course.id;
            """
            
            # Fetch the data and store it in a DataFrame
            df = pd.read_sql(query, connection)
            return df

    except Error as e:
        print(f"Error connecting to the database or executing query: {e}")
        return None

    finally:
        # Ensure the connection is closed if it was established
        if connection is not None and connection.is_connected():
            connection.close()
            print("Database connection closed")

# Fetch and display the data
df = fetch_course_registration_data()
if df is not None:
    print(df.head())
