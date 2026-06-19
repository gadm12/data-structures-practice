def rot13(message):

    ciphered = ""
    for char in message:
        if char.isalpha():
            if "a" <= char <= "m":
                char = ord(char)
                val = char + 13
                coded = chr(val)
                ciphered += coded
            elif "n" <= char <= "z":
                char = ord(char)
                val = char - 13
                coded = chr(val)
                ciphered += coded
            elif "A" <= char <= "M":
                char = ord(char)
                val = char + 13
                coded = chr(val)
                ciphered += coded
            elif "N" <= char <= "Z":
                char = ord(char)
                val = char - 13
                coded = chr(val)
                ciphered += coded
        else:
            ciphered += char
    return ciphered


print(rot13("aA bB zZ 1234 *!?%'"))


