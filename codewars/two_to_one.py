def longest(a1, a2):

    c = ""

    for char in a1 + a2:
        if char not in c:
            c += char

    return "".join(sorted(c))


print(longest("aretheyhere", "yestheyarehere"))
