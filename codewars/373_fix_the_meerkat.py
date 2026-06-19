def fix_the_meerkat(arr):

    for i in range(len(arr)):
        arr[0], arr[2] = arr[2], arr[0]

    return arr


print(fix_the_meerkat(["tail", "body", "head"]))
