# ASIF-IKM-Assisment

Run the following script in MSSQL Management Server:

CREATE TABLE customers (
  id INT NOT NULL PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  email VARCHAR(255) NOT NULL,
  phone VARCHAR(20) NULL
);

 

CREATE TABLE orders (
  id INT NOT NULL PRIMARY KEY,
  customer_id INT NOT NULL,
  total_price DECIMAL(10, 2) NOT NULL,
  created_at DATETIME NOT NULL,
  CONSTRAINT fk_orders_customers FOREIGN KEY (customer_id) REFERENCES customers(id)
);

 

CREATE TABLE products (
  id INT NOT NULL PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  price DECIMAL(10, 2) NOT NULL
);

Again Run this script in MSSQL Management Server:

INSERT INTO customers (id, name, email, phone)
VALUES (1, 'John Doe', 'john.doe@example.com', NULL),
       (2, 'Jane Smith', 'jane.smith@example.com', '555-1234'),
       (3, 'Bob Johnson', 'bob.johnson@example.com', '555-5678');

 
INSERT INTO orders (id, customer_id, total_price, created_at)
VALUES (1, 1, 100.00, '2022-01-01 10:00:00'),
       (2, 1, 50.00, '2022-01-02 11:00:00'),
       (3, 2, 75.00, '2022-01-03 12:00:00'),
       (4, 3, 200.00, '2022-01-04 13:00:00');

INSERT INTO products (id, name, price)
VALUES (1, 'Product A', 10.00),
       (2, 'Product B', 20.00),
       (3, 'Product C', 30.00);


Run the following in CMD  
 **_pip install requirements.txt_**
