import sqlite3
import csv

# Connect to the SQLite database
conn = sqlite3.connect('drivers.db')

# Create a cursor object
cursor = conn.cursor()

# Execute a SQL query to fetch data from the table
cursor.execute('SELECT * FROM driver_info_1')

# Fetch all rows from the table
data = cursor.fetchall()

# Define the CSV file name
csv_file_name = 'driver_info_1.csv'

# Define the CSV column headers
csv_headers = ['DriverAge1', 'LicenceType', 'DeclineReason', 'Acceptable', 'ProvisFlag']

# Write the data to the CSV file
with open(csv_file_name, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)

    # Write the header row
    csv_writer.writerow(csv_headers)

    # Write the data rows
    csv_writer.writerows(data)

# Close the database connection
conn.close()

print(f'Data exported to {csv_file_name}')
