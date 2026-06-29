def accum(st):

    # res = []
    # for s in range(len(st)):
    #     res.append(st[s].upper() + st[s].lower() * (s))

    return "-".join(s.upper() + s.lower() * i for i, s in enumerate(st))


print(accum("abcd"))
