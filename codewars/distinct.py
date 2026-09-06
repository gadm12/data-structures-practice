def distinct(seq):

    seen = []
    for num in seq:
        if num not in seen:
            seen.append(num)
    return seen
    # return list(set(seq))


print(distinct([1, 1, 1, 2, 3, 4, 5]))
