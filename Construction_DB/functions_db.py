import sqlite3
import random


def connect_db(db_name):
    """Establish a connection to the SQLite database."""
    conn = sqlite3.connect(db_name)
    return conn


def execute_query(conn, query):
    """Execute a given SQL query using the provided database connection."""
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()


def check_table_exists(conn, table_name):
    """Check if a table exists in the SQLite database."""
    cursor = conn.cursor()
    cursor.execute(f"SELECT count(name) FROM sqlite_master WHERE type='table' AND name='{table_name}'")
    if cursor.fetchone()[0] == 1:
        return True
    return False


# Below is the functions that will define the generation rules for the Driver Age DB

def generate_acceptable_entries_col_1(num_entries=5000):
    acceptable_entries = []
    for _ in range(num_entries):
        age = random.randint(17, 90)
        acceptable_entries.append((age, 'F', '', True, False))  # Empty reason for acceptable entries
    return acceptable_entries


def generate_unacceptable_entries_col_1(num_entries=1000):
    unacceptable_entries = []
    for _ in range(num_entries):
        # Age is either 17 or between 91 and 101
        age = 17 if random.random() < 0.5 else random.randint(91, 101)
        unacceptable_entries.append((age, 'F', 'Decline - Driver Age', False, False))  # Specific decline reason
    return unacceptable_entries


def generate_acceptable_entries_col_2(num_entries=2000):
    acceptable_entries = []
    for _ in range(num_entries):
        age = random.randint(17, 25)
        acceptable_entries.append((age, 'P', '', True, True))  # License 'P', ProvisFlag True
    return acceptable_entries


def generate_unacceptable_entries_col_2(num_entries=1000):
    unacceptable_entries = []
    for _ in range(num_entries):
        age = random.randint(26, 100)  # Assuming upper limit of 100 for simplicity
        unacceptable_entries.append((age, 'P', 'Decline - Driver Age', False, True))  # License 'P', ProvisFlag True
    return unacceptable_entries


def display_table_data(conn, table_name):
    """Fetches and prints all the data from a specified table."""
    try:
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM {table_name}")
        rows = cursor.fetchall()

        # Check if the table is not empty
        if rows:
            print(f"Data from {table_name}:")
            for row in rows:
                print(row)
        else:
            print(f"The table {table_name} is empty.")

    except Exception as e:
        print(f"An error occurred while fetching data from {table_name}: {e}")
