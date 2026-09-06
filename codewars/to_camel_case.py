def to_camel_case(text):

    if text == "":
        return ""
    text = text.replace("-", "_")
    text = text.split("_")
    lst = [text[0]]
    for word in range(1, len(text)):
        lst.append(text[word][0].upper() + text[word][1:])

    return "".join(lst)


print(to_camel_case("The-Stealth-Warrior"))
