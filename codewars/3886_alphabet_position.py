def alphabet_position(text):

    result = []
    for char in text.lower():
        if char.isalpha():
            val = ord(char) - 96
            result.append(str(val))
    return " ".join(result)


print(alphabet_position("The sunset sets at twelve o' clock."))
