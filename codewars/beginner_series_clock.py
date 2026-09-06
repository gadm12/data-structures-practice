def past(h, m, s):

    h = 60 * 60 * 1000 * h
    m = 60 * 1000 * m
    s = 1000 * s
    return h + m + s


print(past(0, 1, 1))
