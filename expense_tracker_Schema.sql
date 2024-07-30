CREATE DATABASE expense_tracker;

USE expense_tracker;

CREATE TABLE categories (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

CREATE TABLE transactions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    amount DECIMAL(10, 2) NOT NULL,
    category_id INT,
    date DATE NOT NULL,
    description TEXT,
    FOREIGN KEY (category_id) REFERENCES categories(id)
);