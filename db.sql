CREATE TABLE expenses (
    id INT AUTO_INCREMENT PRIMARY KEY,
    category VARCHAR(255),
    amount DECIMAL(10, 2),
    date DATE
);


INSERT INTO expenses (category, amount, date)
VALUES ('Food', 25.50, '2025-01-10'),
       ('Travel', 100.00, '2025-01-12'),
       ('Entertainment', 50.00, '2025-01-13');


SELECT * FROM expenses;