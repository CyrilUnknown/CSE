import csv


def validate(num: str):
    if is_first_num_odd(num) and is_second_num_even(num):
        return True
    return False


def divisible_by_three(num: str):
    first_num = int(num[0])    # This is the first number
    if first_num % 3 == 0:
        return True
    return False


def divisible_by_2(num: str):
    first_num = int(num[0])    # This is the first number
    if first_num % 2 == 0:
        return True
    return False


def is_first_num_odd(num: str):
    first_num = int(num[0])
    if first_num % 2 == 1:
        return True
    return False


def is_second_num_even(num: str):
    second_num = int

#  with open("Book1.csv", 'r') as old_csv:
#       reader = csv.reader(old_csv)
#       for row in reader:
#           old_number = row[0]
#           # print(int(old_number) + 1)
#           print(old_number)


with open("Book1.csv", 'r') as old_csv:
    with open("MyNewBestFile", "w", newline='') as new_csv:
        reader = csv.reader(old_csv)
        writer = csv.writer(new_csv)
        print("Processing...")

        for row in reader:
            old_number = row[0]
        if validate(old_number):
            writer.writerow(row)
        print("OK")
