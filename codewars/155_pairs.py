def pairs(arr):
    # return # of consecutive pairs

    count = 0

    # loop in range of arr
    for i in range(0, len(arr) - 1, 2):

        if arr[i] + 1 == arr[i + 1] or arr[i] - 1 == arr[i + 1]:
            count += 1

    return count


print(pairs([1, 2, 5, 8, -4, -3, 7, 6, 5]))
