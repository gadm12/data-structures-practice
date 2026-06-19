def abbrev_name(name):

    lst = list(name.split(" "))

    return f"{lst[0][0].upper()}.{lst[1][0].upper()}"


print(abbrev_name("Sam Harris"))
