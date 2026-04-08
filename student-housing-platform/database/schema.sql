CREATE DATABASE IF NOT EXISTS student_housing;
USE student_housing;

CREATE TABLE listings (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    location VARCHAR(255) NOT NULL,
    price INT NOT NULL,
    trust INT DEFAULT 0,
    lat DECIMAL(10, 7),
    lng DECIMAL(10, 7),
    image VARCHAR(255),
    phone VARCHAR(15),
    description TEXT
);

CREATE TABLE reviews (
    id INT AUTO_INCREMENT PRIMARY KEY,
    listing_id INT,
    rating INT,
    comment TEXT,
    FOREIGN KEY (listing_id) REFERENCES listings(id)
);

CREATE TABLE reports (
    id INT AUTO_INCREMENT PRIMARY KEY,
    listing_id INT,
    reason TEXT
);