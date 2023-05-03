import pyodbc
import psycopg2
from datetime import datetime
import logging
logging.basicConfig(level=logging.INFO)

# PostgreSQL's connection details
connecting_postgres = psycopg2.connect(
    host="localhost",
    database="Ecomerce_Data",
    user="postgres",
    password="1234")

# SQL Server connection details
connecting_sql = pyodbc.connect("Driver={SQL Server};"
                                "Server=.;"
                                "Database=Ecomerce_Data;"
                                "Trusted_Connection=yes;")


def postgress_migration_customer():
    # Create a cursor for SQL Server and PostgresSQL
    postgres_cursor = connecting_postgres.cursor()
    sqlserver_cursor = connecting_sql.cursor()

    logging.info("Migration started for Customer")
    # Execute a SELECT statement on SQL Server
    customer = sqlserver_cursor.execute('SELECT * FROM customers')

    count = 0
    for row in customer.fetchall():
        count += 1
        name = row[1] if row[1] != None else ""
        email = row[2] if row[2] != None else ""
        postgres_cursor.execute(
            f"INSERT INTO customers (id,name,email,phone) VALUES ('{row[0]}','{name}','{email}','{row[3]}')",
        )
        connecting_postgres.commit()
    logging.info(f"{count} rows Migrated")
    sqlserver_cursor.close()
    postgres_cursor.close()


def postgress_migration_orders():
    # Create a cursor for SQL Server and PostgresSQL
    postgres_cursor = connecting_postgres.cursor()
    sqlserver_cursor = connecting_sql.cursor()

    logging.info("Migration started for Orders")
    # Execute a SELECT statement on SQL Server
    orders = sqlserver_cursor.execute('SELECT * FROM orders')

    count = 0
    for row in orders.fetchall():
        count += 1
        total_price = row[2] if row[2] != None else 0
        created_at = row[3] if row[3] != None else datetime.now()
        postgres_cursor.execute(
            f"INSERT INTO orders (id,customer_id,total_price,created_at) VALUES ('{row[0]}','{row[1]}','{total_price}','{created_at}')",
        )
        connecting_postgres.commit()
    logging.info(f"{count} rows Migrated")
    sqlserver_cursor.close()
    postgres_cursor.close()


def postgress_migration_products():
    # Create a cursor for SQL Server and PostgresSQL
    postgres_cursor = connecting_postgres.cursor()
    sqlserver_cursor = connecting_sql.cursor()

    logging.info("Migration started for Orders")
    products = sqlserver_cursor.execute('SELECT * FROM products')

    count = 0
    for row in products.fetchall():
        count += 1
        name = row[1] if row[1] != None else ""
        price = row[2] if row[2] != None else 0
        postgres_cursor.execute(
            f"INSERT INTO products (id,name,price) VALUES ('{row[0]}','{name}','{price}')",
        )
        connecting_postgres.commit()
    logging.info(f"{count} rows Migrated")
    sqlserver_cursor.close()
    postgres_cursor.close()


if __name__ == '__main__':
    postgress_migration_customer()
    postgress_migration_orders()
    postgress_migration_products()
