from functions_db import connect_db, execute_query, check_table_exists
from functions_db import generate_acceptable_entries_col_1, generate_unacceptable_entries_col_1
from functions_db import generate_acceptable_entries_col_2, generate_unacceptable_entries_col_2
import logging

# Configure basic logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def create_driver_info_table():
    # SQL query to create the driver_info table
    create_table_query = '''
    CREATE TABLE IF NOT EXISTS driver_info_1 (
        DriverAge1 INTEGER,
        LicenceType TEXT,
        DeclineReason TEXT,
        Acceptable BOOLEAN,
        ProvisFlag BOOLEAN
    );
    '''

    # Establish a connection to the database
    conn = connect_db('drivers.db')

    # Check if the table already exists
    if not check_table_exists(conn, 'driver_info_1'):
        # Execute the query if the table does not exist
        execute_query(conn, create_table_query)
        print("Table created successfully.")
    else:
        print("Table already exists.")

    # Close the connection
    conn.close()


def insert_data_into_table():
    try:
        # Generate entries
        logging.info("Generating data...")
        acceptable1 = generate_acceptable_entries_col_1()
        unacceptable1 = generate_unacceptable_entries_col_1()
        acceptable2 = generate_acceptable_entries_col_2()
        unacceptable2 = generate_unacceptable_entries_col_2()

        # Combine all entries
        all_entries = acceptable1 + unacceptable1 + acceptable2 + unacceptable2

        # Establish a connection to the database
        conn = connect_db('drivers.db')

        logging.info("Inserting data into the database...")
        # Insert each entry into the driver_info_1 table
        for entry in all_entries:
            age, licence, decline_reason, acceptable, provis_flag = entry
            insert_query = f"""INSERT INTO driver_info_1 (DriverAge1, LicenceType, DeclineReason, Acceptable, ProvisFlag)
                               VALUES ({age}, '{licence}', '{decline_reason}', {acceptable}, {provis_flag});"""
            execute_query(conn, insert_query)

        # Close the connection
        conn.close()
        logging.info("Data insertion complete.")

    except Exception as e:
        logging.error(f"An error occurred: {e}")


# Call the function to create the table
create_driver_info_table()
insert_data_into_table()
