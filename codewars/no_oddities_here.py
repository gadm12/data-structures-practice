def no_odds(values):

    lst = []
    for v in range(len(values)):
        if values[v] % 2 == 0:
            lst.append(values[v])
    return lst


print(no_odds([0, 2, 4, 6, 8, 10]))
print(no_odds([1, 3, 5, 7, 9]))
print(no_odds([-1, -3, -5, -7, -9]))
print(no_odds([2, 4, 8, 6, 0]))
