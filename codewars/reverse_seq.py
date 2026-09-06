def reverse_seq(n):

    lst = []
    for i in range(1, n + 1):
        lst.append(i)
    return lst[::-1]


print(reverse_seq(5))
