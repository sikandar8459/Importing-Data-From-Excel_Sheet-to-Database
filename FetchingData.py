import sqlite3

# Establish a SQLite3 connection & creating database
conn = sqlite3.connect("ImportingData.db")

# Creating cursor 
cur = conn.cursor()

# Creating function to fetch all data
def fetch_data():

    # Executing query
    cur.execute("select * from Excel_Database")

    # Storing all data into a variable
    result = cur.fetchall()

    # Using for loop to print the data
    for row in result:
        print(f"Programming Language is {row[1]} and Developed by {row[2]}.")

fetch_data()