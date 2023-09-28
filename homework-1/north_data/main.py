"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
import csv

conn = psycopg2.connect(host='localhost', database='north', user='postgres', password='373479060')
try:
    with conn:
        with conn.cursor() as cur:
            with open('customers_data.csv', 'r', newline="", encoding='UTF-8') as file:
                reader = csv.reader(file)
                next(reader)
                for row in reader:
                    cur.execute("INSERT INTO customers VALUES (%s, %s, %s)", row)
                conn.commit()
finally:
    conn.close()

try:
    with conn:
        with conn.cursor() as cur:
            with open('employees_data.csv', 'r', newline="", encoding='UTF-8') as csvfile:
                employee_reader = csv.reader(csvfile)
                next(employee_reader)
                for r in employee_reader:
                    cur.execute("INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)", r)
                conn.commit()
finally:
    conn.close()

try:
    with conn:
        with conn.cursor() as cur:
            with open('orders_data.csv', 'r', newline="", encoding='UTF-8') as csv_file:
                orders_reader = csv.reader(csv_file)
                next(orders_reader)
                for line_ in orders_reader:
                    cur.execute("INSERT INTO orders VALUES (%s, %s, %s, %s, %s)", line_)
                conn.commit()
finally:
    conn.close()