def find_uniq(arr):

    if arr[0] == arr[1]:
        common = arr[0]
    elif arr[0] == arr[2]:
        common = arr[0]
    else:
        common = arr[1]
    for num in arr:
        if num != common:
            return num


print(find_uniq([1, 1, 1, 2, 1, 1]))
