CREATE DATABASE event_decor;
USE event_decor;

-- Admin Table
CREATE TABLE admin (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50),
    password VARCHAR(50)
);

INSERT INTO admin VALUES (1,'admin','admin123');

-- Booking Table
CREATE TABLE bookings (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    phone VARCHAR(15),
    event_type VARCHAR(50),
    event_date DATE,
    message TEXT
);

-- Media Table (Images & Videos)
CREATE TABLE media (
    id INT AUTO_INCREMENT PRIMARY KEY,
    file_name VARCHAR(255),
    file_type VARCHAR(20)
);
