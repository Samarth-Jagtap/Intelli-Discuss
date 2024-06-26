import streamlit as st
import pandas as pd
import psycopg2
from psycopg2 import Error
import logging
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)

# Load configuration values from environment variables
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Configure Genai Key
genai.configure(api_key=GOOGLE_API_KEY)

# Function to connect to PostgreSQL database
def connect_to_db():
    try:
        conn = psycopg2.connect(
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )
        return conn
    except Error as e:
        logger.error(f"Error connecting to PostgreSQL database: {e}")
        st.error(f"Error connecting to PostgreSQL database: {e}")
        return None

# Function to create table and insert data
def insert_data_into_db(conn, table_name, df):
    cursor = conn.cursor()
    try:
        # Infer data types from the dataframe
        dtypes = df.dtypes
        
        # Create table with appropriate data types
        create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} ("
        for col_name, dtype in dtypes.items():
            sql_type = ""
            if dtype == 'int64':
                sql_type = "BIGINT"
            elif dtype == 'float64':
                sql_type = "REAL"
            elif dtype == 'object':
                # Assuming all other types are strings
                sql_type = "TEXT"
            create_table_query += f'"{col_name.lower().replace(" ", "_")}" {sql_type}, '  # Convert to lowercase and replace spaces with underscores
        create_table_query = create_table_query.rstrip(', ') + ");"
        
        cursor.execute(create_table_query)

        # Insert data into the table
        column_names = ', '.join(['"' + col.lower().replace(" ", "_") + '"' for col in df.columns])  # Convert to lowercase and replace spaces with underscores
        placeholders = ', '.join(['%s'] * len(df.columns))
        insert_query = f"INSERT INTO {table_name} ({column_names}) VALUES ({placeholders})"
        for index, row in df.iterrows():
            cursor.execute(insert_query, tuple(row))
        
        conn.commit()
        st.success("Data inserted into database successfully!")
    except Error as e:
        conn.rollback()
        logger.error(f"Error inserting data into database: {e}")
        st.error(f"Error inserting data into database: {e}")
    finally:
        cursor.close()

# Function to delete all tables from the database
def delete_all_tables_from_db(conn):
    cursor = conn.cursor()
    try:
        # Fetch all table names
        cursor.execute("""
        SELECT table_name
        FROM information_schema.tables
        WHERE table_schema='public'
        """)
        tables = cursor.fetchall()
        
        # Drop each table
        for table in tables:
            drop_table_query = f"DROP TABLE IF EXISTS {table[0]} CASCADE"
            cursor.execute(drop_table_query)
        
        conn.commit()
        st.success("All tables deleted successfully!")
    except Error as e:
        conn.rollback()
        logger.error(f"Error deleting tables: {e}")
        st.error(f"Error deleting tables: {e}")
    finally:
        cursor.close()

# Function to load Google Gemini Model and provide queries as response
def get_gemini_response(question, prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt, question])
    return response.text.strip()  # Remove leading/trailing whitespaces

# Function to execute a query and display the output
def execute_query(conn, query):
    cursor = conn.cursor()
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]
        df = pd.DataFrame(result, columns=columns)
        st.write(df)
    except Error as e:
        logger.error(f"Error executing query: {e}")
        st.error(f"Error executing query: {e}")
    finally:
        cursor.close()

def upload_csv_file():
    uploaded_file = st.file_uploader("Upload CSV", type=["csv"])
    return uploaded_file

def preview_csv_data(uploaded_file):
    df = pd.read_csv(uploaded_file)
    st.write(df.head())
    return df

def get_table_name():
    table_name = st.text_input("Enter table name to insert data into:", "first")
    return table_name.lower().replace(" ", "_")

def main():
    st.title("Upload CSV And Ask")

    uploaded_file = upload_csv_file()
    if uploaded_file is not None:
        st.subheader("Preview CSV Data")
        df = preview_csv_data(uploaded_file)

        conn = connect_to_db()

        if conn is not None:
            table_name = get_table_name()
            if st.button("Insert Data into Database"):
                insert_data_into_db(conn, table_name, df)

            st.subheader("Execute a Query")
            query_input = st.text_input("Enter a query in English:")
            if query_input:
                # Provide instructions to the user
                st.write("Please wait while we generate the SQL query...")
                
                # Prepare the prompt for Gemini
                columns = [col.lower().replace(" ", "_") for col in df.columns]
                prompt = f"""
                You are an expert in converting English questions to SQL query!
                The SQL database has the table {table_name} with the following columns - {', '.join(columns)}.

                For example:
                Example 1 - How many entries of records are present?
                The SQL command will be something like this: SELECT COUNT(*) FROM {table_name} ;

                Example 2 - Show me all the countries with a score greater than 7.6.
                The SQL command will be something like this: SELECT country_or_region FROM {table_name} WHERE score > 7.6; 
                Also, the SQL code should not have ``` in beginning or end and sql word in output.
                """
                
                # Generate SQL query using Gemini
                sql_query = get_gemini_response(query_input, prompt)
                st.write("Generated SQL Query:", sql_query)
                
                # Execute the SQL query
                if st.button("Execute Query"):
                    # Adjust column names in the SQL query
                    sql_query_adjusted = sql_query.replace("Country or region", "country_or_region")
                    execute_query(conn, sql_query_adjusted)

            st.subheader("Delete All Tables")
            if st.button("Delete All Tables"):
                delete_all_tables_from_db(conn)

            conn.close()

if __name__ == "__main__":
    main()
