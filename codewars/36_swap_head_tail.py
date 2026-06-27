def swap_head_tail(arr):

    mid = len(arr) // 2
    if len(arr) % 2 == 0:
        return arr[mid:] + arr[:mid]
    else:
        return arr[mid + 1 :] + [arr[mid]] + arr[:mid]


print(swap_head_tail([1, 2, 3, 4, 5]))
