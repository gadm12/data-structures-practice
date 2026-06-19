def get_count(sentence):

    vowels = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}
    for char in sentence:
        if char in vowels:
            vowels[char] += 1
    return sum(vowels.values())


print(get_count("aeiou"))
