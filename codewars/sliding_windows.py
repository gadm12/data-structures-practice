#sliding windows
def window(lngth, offst, lst):
    new = []

    left = 0

    while left + lngth <= len(lst):
        right = left + lngth
        new.append(lst[left:right])
        left += offst
    return new


print(window(2, 1, [0, 1, 2, 3, 4]))
