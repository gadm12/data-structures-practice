def binary_array_to_number(arr):

    string = []

    for char in arr:
        string.append(str(char))
    integer = int("".join(string), 2)

    return integer


print(binary_array_to_number([1, 1, 1, 1]))
