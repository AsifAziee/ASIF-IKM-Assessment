-- Sample data for the customers table in SQL Server
INSERT INTO customers (id, name, email, phone)
VALUES (1, 'John Doe', 'john.doe@example.com', NULL),
       (2, 'Jane Smith', 'jane.smith@example.com', '555-1234'),
       (3, 'Bob Johnson', 'bob.johnson@example.com', '555-5678');

-- Sample data for the orders table in SQL Server
INSERT INTO orders (id, customer_id, total_price, created_at)
VALUES (1, 1, 100.00, '2022-01-01 10:00:00'),
       (2, 1, 50.00, '2022-01-02 11:00:00'),
       (3, 2, 75.00, '2022-01-03 12:00:00'),
       (4, 3, 200.00, '2022-01-04 13:00:00');

-- Sample data for the products table in SQL Server
INSERT INTO products (id, name, price)
VALUES (1, 'Product A', 10.00),
       (2, 'Product B', 20.00),
       (3, 'Product C', 30.00);
