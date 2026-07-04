def small_enough(array, limit):

    for num in array:
        if num > limit:
            return False
    return True


print(small_enough([78, 33, 22, 44, 88, 9, 6], 87))

print(small_enough([1, 2, 3, 4, 5, 6, 7, 8, 9], 10))
