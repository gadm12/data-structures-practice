def duplicate_count(text):

    count = {}
    duplicates = 0

    for char in text.lower():
        if char not in count:

            count[char] = 1

        else:
            count[char] += 1
    for v in count.values():
        if v > 1:
            duplicates += 1

    return duplicates


print(duplicate_count("abcdeaa"))
