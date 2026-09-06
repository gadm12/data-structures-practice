def is_isogram(string):

    seen = ""

    for char in string.lower():
        if char in seen:
            return False

        seen += char
    return True


print(is_isogram("Dermatoglyphics"))
print(is_isogram("isIsogram"))
