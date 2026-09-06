def sum_array(arr):

    if arr is None or len(arr) <= 2:
        return 0

    smallest = arr[0]
    highest = arr[0]
    total = 0
    for num in arr:
        if num < smallest:
            smallest = num
        elif num > highest:
            highest = num
        total += num
    return total - (highest + smallest)


print(sum_array([6, 2, 1, 8, 10]))
print(sum_array([6, 2]))
