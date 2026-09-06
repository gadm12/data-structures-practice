def binary_cleaner(seq):

    lst_1 = []
    lst_2 = []

    for i in range(len(seq)):
        if seq[i] < 2:
            lst_1.append(seq[i])
        if seq[i] > 1:
            lst_2.append(i)

    return lst_1, lst_2


print(binary_cleaner([0, 1, 2, 1, 0, 2, 1, 1, 1, 0, 4, 5, 6, 2, 1, 1, 0]))
print(binary_cleaner([0, 1, 2, 1, 5, 6, 2, 1, 1, 0]))
