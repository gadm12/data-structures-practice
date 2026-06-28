def db_sort(arr):
    nums = []
    strings = []
    for i in arr:
        if isinstance(i, (int, float)):
            nums.append(i)
        else:
            strings.append(i)

    nums.sort()
    strings.sort()

    return nums + strings  #


print(db_sort(["come", "on", 110, "2500", 10, "!", 7, 15, 5, 6, 6]))
