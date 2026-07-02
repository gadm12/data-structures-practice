def stray(arr):
    min()
    counter = {}

    for n in arr:
        counter[n] = counter.get(n, 0) + 1
    for k, v in counter.items():
        if v == 1:
            return k


print(stray([1, 1, 1, 1, 1, 1, 2]))
