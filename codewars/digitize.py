def digitize(n):
    # int_lst = []
    # lst = list(str(n))[::-1]
    # for char in lst:
    #     int_lst.append(int(char))
    # return int_lst
    return [int(x) for x in list(str(n)[::-1])]



print(digitize(23582357))
