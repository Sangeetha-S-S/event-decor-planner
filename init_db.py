import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

# Create bookings table
cursor.execute("""
CREATE TABLE IF NOT EXISTS bookings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    phone TEXT,
    address TEXT,
    email TEXT,
    event_type TEXT,
    event_date TEXT,
    message TEXT,
    decor_image TEXT,
    package_price INTEGER,
    status TEXT DEFAULT 'Pending'
)
""")

# Create contact table
cursor.execute("""
CREATE TABLE IF NOT EXISTS contact_us (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT,
    phone TEXT,
    message TEXT
)
""")

conn.commit()
conn.close()

print("Database created successfully")