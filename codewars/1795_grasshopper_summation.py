def summation(num):

    total = 0

    while num > 0:
        total = num + total
        num -= 1
    return total


print(summation(8))
