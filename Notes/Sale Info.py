import csv

with open("Sales Records.csv", 'r') as old_csv:
    reader = csv.reader(old_csv)
    total = 0
    for row in reader:
        old_number = row[13]
        if row[2] == "Fruits":
            num = float(old_number)
            total += num
            # print(old_number)
