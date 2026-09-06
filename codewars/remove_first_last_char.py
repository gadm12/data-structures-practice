def remove_char(s):

    word = list(s)
    word.pop(0)
    word.pop(-1)

    # return s[1:-1]
    return "".join(word)


print(remove_char("eloquent"))
print(remove_char("country"))
