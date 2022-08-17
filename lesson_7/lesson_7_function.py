

list_of_num = [1, 2, 3, 4, 3, 2, 2, 3, 2, 1]


def frequency_num(b):
    dict_num = {}
    for item in b:
        if item in dict_num:
            dict_num[item] += 1
        else:
            dict_num[item] = 1
    return dict_num


print(frequency_num(list_of_num))