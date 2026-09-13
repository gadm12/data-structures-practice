def largest_pair_sum(numbers):

    lst = sorted(numbers, reverse=True)
    return lst[0] + lst[1]


print(largest_pair_sum([10, 14, 2, 23, 19]))
