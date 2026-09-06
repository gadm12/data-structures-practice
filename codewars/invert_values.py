def invert(array):
    inverted_array = []
    for num in array:
        inverted_array.append(-num)
    return inverted_array


print(invert([1, 2, 3, 4, 5]))
