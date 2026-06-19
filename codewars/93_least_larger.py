def least_larger(a, i):

    largest_num = []

    largest = a[i]
    for num in a:
        if num > largest:
            largest_num.append(num)
    if not largest_num:
        return -1
    else:
        smallest = largest_num[0]
        for n in largest_num:
            if n < smallest:
                smallest = n

    return a.index(smallest)


print(least_larger([4, 1, 3, 5, 6], 4))
