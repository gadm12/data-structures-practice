def disemvowel(string_):
    vowels = {"a", "e", "i", "o", "u"}
    results = ""
    for char in string_:
        if char.lower() not in vowels:
            results += char

    return results


print(disemvowel("This website is for losers LOL!"))
