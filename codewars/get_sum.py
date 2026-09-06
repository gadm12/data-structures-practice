def get_sum(a, b):
    if a == b:
        return a
    sum = 0
    for n in range(min(a, b), max(a, b) + 1):
        print(n)
        sum += n
    return sum


print(get_sum(-1, 3))
print(get_sum(3, -1))
