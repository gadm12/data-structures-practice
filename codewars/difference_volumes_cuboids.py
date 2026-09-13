def find_difference(a, b):

    a_volume = 1
    b_volume = 1

    for n in a:
        a_volume *= n
    for n in b:
        b_volume *= n
    return abs(a_volume - b_volume)


print(find_difference([3, 2, 5], [1, 4, 4]))
print(find_difference([9, 7, 2], [5, 2, 2]))
