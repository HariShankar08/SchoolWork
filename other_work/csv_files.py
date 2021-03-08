import csv


with open('one.csv', 'w', newline='') as file:
    writer = csv.writer(file, delimiter='\t')
    writer.writerow(['S.No', 'Name', 'Mark'])  # Write a single row, single list
    rows = [[1, 'A', 2], [2, 'B', 3]]
    writer.writerows(rows)  # writerows - requires a nested list as in var row

with open('one.csv', newline='') as file:
    reader = csv.reader(file, delimiter='\t')
    for row in reader:
        print(row)  # Every data item is converted to a STRING


