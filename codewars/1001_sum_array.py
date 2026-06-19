def sum_array(a):

    if len(a) == 0:
        return 0
    counter = 0
    for i in a:
        counter = counter + i
    return counter


print(sum_array([1.1, 2.2, 3.3]))
print(sum_array([]))
