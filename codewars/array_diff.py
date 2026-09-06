def array_diff(a, b):

    c = []

    for num in a:
        if num not in b:
            c.append(num)

    return c


print(array_diff([1, 2, 2], [1]))
