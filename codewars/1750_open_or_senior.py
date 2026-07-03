def open_or_senior(data):

    lst = []
    for d in data:
        if d[0] >= 55 and d[1] > 7:
            lst.append("Senior")
        else:
            lst.append("Open")

    return lst


print(open_or_senior([(45, 12), (55, 21), (19, -2), (104, 20)]))
