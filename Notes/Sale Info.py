import csv

with open("Sales Records.csv", 'r') as old_csv:
    reader = csv.reader(old_csv)
    fruit_total = 0
    clothes_total = 0
    meat_total = 0
    beverages_total = 0
    office_supplies_total = 0
    cosmetics_total = 0
    snack_total = 0
    personal_care_total = 0
    household_total = 0
    vegetables_total = 0
    baby_food_total = 0
    cereal_total = 0
    num = 0
    for row in reader:
        old_number = row[13]
        try:
            num = float(old_number)
        except ValueError:
            num = num
        if row[2] == "Fruits":
            fruit_total += num
        elif row[2] == "Clothes":
            clothes_total += num
        elif row[2] == "Meat":
            meat_total += num
        elif row[2] == "Beverages":
            beverages_total += num
        elif row[2] == "Office Supplies":
            office_supplies_total += num
        elif row[2] == "Cosmetics":
            cosmetics_total += num
        elif row[2] == "Snacks":
            snack_total += num
        elif row[2] == "Personal Care":
            personal_care_total += num
        elif row[2] == "Household":
            household_total += num
        elif row[2] == "Vegetables":
            vegetables_total += num
        elif row[2] == "Baby Food":
            baby_food_total += num
        elif row[2] == "Cereal":
            cereal_total += num
Items = [Fruits, Clothes, Meat, Beverages, Office Supplies, Cosmetics,
         Snack, Personal Care, Household, Vegetables, Baby Food, Cereal]
print(fruit_total)
print(clothes_total)
print(meat_total)
print(beverages_total)
print(office_supplies_total)
print(cosmetics_total)
print(snack_total)
print(personal_care_total)
print(household_total)
print(vegetables_total)
print(baby_food_total)
print(cereal_total)
