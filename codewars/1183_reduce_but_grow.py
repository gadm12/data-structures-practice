def grow(arr):

    counter = 1
    for i in arr:
        counter = counter * i
    return counter


print(grow([1, 2, 3, 4]))
