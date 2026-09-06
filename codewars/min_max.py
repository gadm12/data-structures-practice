def min_max(lst):

    smallest = lst[0]
    largest = lst[0]
    for num in lst:
        if num < smallest:
            smallest = num
        if num > largest:
            largest = num
    return [smallest, largest]


print(min_max([1,2,3,4,5]))
