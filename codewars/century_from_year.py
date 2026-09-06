def century(year):

    remaining = year % 100
    cen = year // 100
    if remaining == 0:
        return cen
    else:
        return cen + 1


print(century(1705))


