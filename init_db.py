import sqlite3
import os

def initialize():
    connection = sqlite3.connect("database.db")
    
    # Read the updated SQL file
    with open('database.sql') as f:
        connection.executescript(f.read())
        
    connection.commit()
    connection.close()
    print("Database initialized with correct tables!")

if __name__ == "__main__":
    initialize()