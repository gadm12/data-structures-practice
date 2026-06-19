def to_jaden_case(string):

    words = string.split()
    result = []
    for word in words:
        result.append(word.capitalize())
    return " ".join(result)


quote = "How can mirrors be real if our eyes aren't real"
print(to_jaden_case(quote))
