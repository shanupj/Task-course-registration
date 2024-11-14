import os
import pandas as pd
from sqlalchemy import create_engine

# Load environment variables for database credentials
DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_USER = os.getenv('DB_USER', 'root')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'root')
DB_NAME = os.getenv('DB_NAME', 'courseRegistration')

def fetch_course_registration_data():
    # Create a connection string for SQLAlchemy
    connection_string = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
    engine = create_engine(connection_string)

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
    try:
        df = pd.read_sql(query, engine)
        print("Data fetched successfully")
        return df
    except Exception as e:
        print(f"Error executing query: {e}")
        return None

# Fetch and display the data
df = fetch_course_registration_data()
if df is not None:
    print(df.head())
