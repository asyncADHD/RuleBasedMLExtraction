from functions_db import connect_db, display_table_data

def show_table():
    conn = connect_db('drivers.db')
    display_table_data(conn, 'driver_info_1')
    conn.close()

# Call the function to display the table data
show_table()
