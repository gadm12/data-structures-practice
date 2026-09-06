def sum_average(lists):

    avg = []

    for lst in lists:
        lst_avg = sum(lst) / len(lst)
        avg.append(lst_avg)
    return sum(avg)


print(sum_average([[1, 2, 2, 1], [2, 2, 2, 1]]))
