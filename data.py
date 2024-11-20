import sqlite3

def fetchall():
    # Connect to the Database
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    # Query Data
    cursor.execute('SELECT * FROM files')
    rows = cursor.fetchall()
    # Close Connection
    conn.close()

    return rows

def insert_data(filename):
    # Connect to the Database
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    # Insert Data
    cursor.execute('INSERT INTO files (filename) VALUES (?)',(filename,))
    # Commit changes
    conn.commit()
    # Close Connection
    conn.close()
