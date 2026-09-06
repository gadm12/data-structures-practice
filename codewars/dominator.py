def dominator(arr):

    counts = {}

    for num in arr:
        counts[num] = counts.get(num, 0) + 1
        # if num not in counts:
        #     counts[num] = 1
        # else:
        #     counts[num] += 1
    for k, v in counts.items():
        if v > len(arr) // 2:
            return k

    return -1


print(dominator([3, 4, 3, 2, 3, 1, 3, 3]))
