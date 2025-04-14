CREATE DATABASE IF NOT EXISTS smart_parking;
USE smart_parking;

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS parking_spaces (
    id INT AUTO_INCREMENT PRIMARY KEY,
    space_number VARCHAR(10) NOT NULL UNIQUE,
    location VARCHAR(100) DEFAULT 'Main Parking'
);

CREATE TABLE IF NOT EXISTS reservations (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    space_id INT NOT NULL,
    start_time DATETIME NOT NULL,
    end_time DATETIME NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (space_id) REFERENCES parking_spaces(id) ON DELETE CASCADE
);

INSERT INTO parking_spaces (space_number) VALUES 
('A1'), ('A2'), ('A3'), ('A4'), ('A5'),
('B1'), ('B2'), ('B3'), ('B4'), ('B5'),
('C1'), ('C2'), ('C3'), ('C4'), ('C5');