def gimme(arr):

    l, s = max(arr), min(arr)

    for n in range(len(arr)):
        if arr[n] > s and arr[n] < l:
            return n

    return l, s


print(gimme([5, 10, 14]))
print(gimme([2, 3, 1]))
