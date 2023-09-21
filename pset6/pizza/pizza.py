import sys
import csv
from tabulate import tabulate

if len(sys.argv) != 2 or not sys.argv[1].endswith('.csv'):
    print("Usage: python pizza.py <csv_file>")
    sys.exit(1)

try:
    with open(sys.argv[1], newline='') as csvfile:
        reader = csv.reader(csvfile)

        # Read the header (first row) to get column names
        header = next(reader)

        # Read the data from the CSV file
        data = [row for row in reader]
except FileNotFoundError:
    print(f"File '{sys.argv[1]}' not found.")
    sys.exit(1)

print(tabulate(data, headers=header, tablefmt='grid'))

