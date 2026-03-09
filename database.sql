-- Bookings Table (Updated for SQLite)
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
);

-- Contact Table
CREATE TABLE IF NOT EXISTS contact_us (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT,
    phone TEXT,
    message TEXT
);