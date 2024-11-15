#courseregistration: 
    This Python code is designed to connect to a MySQL database, run a SQL query to fetch course registration data by joining several tables including           account,application,and course. The data is then displayed in a structured format using a Pandas DataFrame.

#Requirements: 
    Python, 
    MySQL server, 
    Pandas and SQLAlchemy Python libraries,
    PyMySQL (MySQL database adapter for Python).
    
You can install the required Python packages using the code:
   " pip install SQLAlchemy pymysql "

#Environment Variables: 
    This program uses environment variables for securely storing database credentials.
    Here are the environment variables and their values:
        DB_HOST:  'localhost' (Hostname of the MySQL server)
        DB_USER:  'root' (MySQL username)
        DB_PASSWORD:  'root' (MySQL password)
        DB_NAME:  'courseRegistration' (Name of the database)

#Database Setup: 
    Before running the program, ensure the following tables exist in the database, as this program will query them. The tables include:
      1. Account: Contains user account information such as email and program.
      2. Application: Stores details about student applications, including application status.
      3. TermCourseRegistrationApplication: Holds course registration details, including the level at which a course is applied.
      4. Course: Contains course information like course name and fee.

#Running the Program: 
    1. Copy the code to a local directory.
    2. Ensure MySQL sever is running and accessible.
    3. Execute the program by running the code:
         " python filename.py "
    4. If successful the data will be displayed in the terminal output as a DataFrame.

#Error Handling: 
    If the program encounters a connection or query execution issue, an error message will be displayed in the terminal. So, ensure that:
      1.Database credentials are correctly set up.
      2.MySQL server is running and accessible.
      3.Required tables exist in the database.
      
