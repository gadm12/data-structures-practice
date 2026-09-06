def tiy_fizz_buzz(string):

    result = ""

    for char in string:
        if char.isupper() and char not in "AEIOU":
            result += "Iron"
        elif char.islower() and char not in "aeiou":
            result += char
        elif char in "AEIOU":
            result += "Iron Yard"
        elif char in "aeiou":
            result += "Yard"
        else:
            result += char
    return result


print(tiy_fizz_buzz("Hello!"))
