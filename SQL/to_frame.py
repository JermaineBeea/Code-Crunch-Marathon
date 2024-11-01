import sqlite3
import pandas as pd

# Connect to the .db file
conn = sqlite3.connect('fiftyville.db')
cursor = conn.cursor()

# List all tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

print("Tables:", [table[0] for table in tables])  # Display table names

# Loop through each table and fetch the data
for table in tables:
    table_name = table[0]
    print(f"\nData from table: {table_name}")
    
    # Fetch all rows from the table and load into a DataFrame
    df = pd.read_sql_query(f"SELECT * FROM {table_name};", conn)
    
    # Display the DataFrame
    print(df)

    # Append DataFrame to CSV file
    df.to_csv('database.csv', mode='a', header=not pd.io.common.file_exists('database.csv'), index=True)

# Close the connection
conn.close()



import sqlite3
import pandas as pd

# Connect to the .db file
conn = sqlite3.connect('fiftyville.db')
cursor = conn.cursor()

# List all tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

print("Tables:", tables)

# Dictionary to hold DataFrames for each table
dataframes = {}

# Loop through each table and fetch the data into a DataFrame
for table in tables:
    table_name = table[0]
    print(f"\nData from table: {table_name}")
    
    # Fetch all rows from the table into a DataFrame
    df = pd.read_sql_query(f"SELECT * FROM {table_name};", conn)
    
    # Store the DataFrame in the dictionary with the table name as key
    dataframes[table_name] = df
    
    # Optionally, print the DataFrame
    print(df)

# Close the connection
conn.close()

# with open('database.csv', 'w') as file:
#     file.write(dataframes)

# Now you can access each DataFrame using dataframes['table_name']
