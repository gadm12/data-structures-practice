def take(arr, n):
    seq = []
    if n <= 0:
        return seq
    else:
        return arr[:n]


print(take([0, 1, 2, 5, 8, 13], 4))
print(take([0, 1, 2, 5, 8, 13], 0))
print(take([], 3))
print(take([0, 1, 2, 5, 8, 13], -3))
