import csv


with open('customers_data.csv', newline="", encoding='UTF-8') as file:
    customers_data = csv.reader(file, delimiter=' ', quotechar='|')
    for row in customers_data:
        print(' '.join(row))

