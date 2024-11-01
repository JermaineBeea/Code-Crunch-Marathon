import sqlite3

# Connect to the database
conn = sqlite3.connect('your_database.db')
cursor = conn.cursor()

# Read and execute the .sql file
with open('your_script.sql', 'r') as file:
    sql_script = file.read()

cursor.executescript(sql_script)

# Commit changes and close the connection
conn.commit()
conn.close()
