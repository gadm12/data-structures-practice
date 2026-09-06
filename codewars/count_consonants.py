def count_consonants(text):

    text = text.lower()

    vowels = "aeiou"
    consonants = set()

    for char in text:
        if char.isalpha() and char not in vowels:
            consonants.add(char)

    return len(consonants)


print(count_consonants("sillystring"))
