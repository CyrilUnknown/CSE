test_num = "4508878827358837"
number_list1 = list(test_num)
print(number_list1)


def validate(num: str):
    if len(number_list1) is not 16:
        print("It doesn't pass")
        return False
    the_last_number = int(num[15])
    my_list = number_list1[0:15][:: -1]
    for index in range(len(my_list)):
        my_list[index] = int(my_list[index])
        if index % 2 == 0:
            my_list[index] *= 2
            if my_list[index] > 9:
                my_list[index] -= 9
    total = sum(my_list)
    return total % 10 == the_last_number


print(validate(test_num))
