def add_length(str_):

    # s = str_.split()
    # lst = []

    # for word in s:

    #     lst.append(word + " " + str(len(word)))
    # return lst
    return [w + " " + str(len(w)) for w in str_.split()]


print(add_length("apple ban"))
