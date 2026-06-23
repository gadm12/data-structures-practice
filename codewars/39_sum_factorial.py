def factorial(n):

    results = 1
    for i in range(1, n + 1):
        results *= i
    return results


def sum_factorial(lst):
    total = 0

    for num in lst:
        total += factorial(num)
    return total


print(sum_factorial([4, 6]))
