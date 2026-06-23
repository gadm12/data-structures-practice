def count_lonely_letters(text):

    letters = []
    for char in text.lower():
        if char.isalpha():
            position = ord(char) - ord("a") + 1
            letters.append(char)
    count = 0
    for char in letters:
        if letters.count(char) == 1:
            prev_letter = chr(ord(char) - 1)
            next_letter = chr(ord(char) + 1)

            if char == "a":
                if "b" not in letters:
                    count += 1
            elif char == "z":
                if "y" not in letters:
                    count += 1
            else:
                if prev_letter not in letters and next_letter not in letters:
                    count += 1

    return count


print(count_lonely_letters("ad"))
print(count_lonely_letters("Hello, World!"))

# letter = ord("c") - ord("a") + 1
# letter_po = chr(letter + ord("a") - 1)
# print(letter)
# print(letter_po)
