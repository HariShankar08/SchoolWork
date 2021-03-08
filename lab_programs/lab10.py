#!/usr/bin/python3.9
import csv

top_level = [['S.No', 'Title', 'Author']]
with open('a_file.csv', 'w', newline='') as file:
    writer = csv.writer(file, delimiter='\t')
    while True:
        s_no = int(input("Enter S.No: "))
        book_name = input("Enter the book name:").strip()
        author = input("Enter the author of the book:").strip()
        top_level.append([s_no, book_name, author])
        if input("Do you want to continue? [Y/n]").strip().lower() == 'n':
            break
        print()
            
    writer.writerows(top_level)

with open('a_file.csv', 'r', newline='') as file:
    reader = csv.reader(file, delimiter='\t')
    for row in reader:
        print(row)

        
        
     
    



