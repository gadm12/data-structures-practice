def name_value(my_list):

    results = []

    for i, word in enumerate(my_list, start=1):
        word_sum = 0
        for char in word:
            if char != " ":
                word_sum += ord(char) - 96
        results.append(word_sum * i)
    return results


print(name_value(["codewars", "abc", "xyz"]))
