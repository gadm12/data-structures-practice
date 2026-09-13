def pillars(num_pill, dist, width):
    if num_pill == 1:
        return 0
    dist = dist * 100
    total = ((dist + width) * (num_pill - 1)) - width

    return total


print(pillars(1, 10, 10))
print(pillars(2, 20, 25))
print(pillars(11, 15, 30))
