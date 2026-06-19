def count_by(x, n):

    # lst = []
    # for i in range(1,n+1):
    #     lst.append(x * i)
    # return lst
    return [x * i for i in range(1, n + 1)]


print(count_by(3, 5))
