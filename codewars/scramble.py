def scramble(strng, array):

    results = [0] * len(strng)

    for s, a in zip(strng, array):
        results[a] = s
    return "".join(results)


print(scramble("abcd", [0, 3, 1, 2]))
