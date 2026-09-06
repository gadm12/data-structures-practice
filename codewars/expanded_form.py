def expanded_form(num):

    parts = []
    num = str(num)

    for i, digit in enumerate(num):
        if digit != "0":
            parts.append(digit + "0" * (len(num) - 1 - i))
    return " + ".join(parts)


print(expanded_form(70304))
