def remove_every_other(my_list):

    new_list = []

    for i in range(0, len(my_list), 2):
        new_list.append(my_list[i])

    return new_list


print(remove_every_other([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
