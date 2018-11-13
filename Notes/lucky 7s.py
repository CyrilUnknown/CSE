import random
money_total = 15
rounds_total = 0
while money_total > 0:
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    add = dice1 + dice2
    rounds_total += 1
    money_total -= 1
    if add == 7:
        money_total += 100
    print(money_total)
    print("You have played %s rounds" % rounds_total)