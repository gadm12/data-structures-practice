def sum_mul(n, m):

    if n < 1 or m < 1:
        return 'INVALID'

    total = 0

    for num in range(n, m, n):

        total += num
    return total


print(sum_mul(2, 9))
print(sum_mul(4, -7))
