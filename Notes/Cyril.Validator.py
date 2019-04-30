test_num = "1947333886071750"
number1 = "1947333886071750"
number_list = list(number1)
print(number_list)
print(len(number_list))

if len(number_list) is not 16:
    print("It doesn't pass")

my_list = number_list[0:15][:: -1]
for index in range(len(my_list)):
    my_list[index] = int(my_list[index])
    if index % 2 == 0:
        my_list[index] *= 2
        if my_list[index] >= 9:
            my_list[index] -= 9
print(my_list)


def validate(num: str):
    pass


print(validate(test_num))