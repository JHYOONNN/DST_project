import csv

with open('201501_all.csv', mode = 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
