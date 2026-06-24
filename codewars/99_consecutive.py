def consecutive(arr):
    if len(arr) <= 1:
        return 0
    diff = (max(arr) - min(arr) + 1) - len(arr)
    print(diff)
    lst = []
    print(max(arr), min(arr))
    for n in range((max(arr) - min(arr) + 1) - len(arr)):
        lst.append(n)

    return len(lst)


print(consecutive([10, -10]))
print(consecutive([4, 8, 6]))
