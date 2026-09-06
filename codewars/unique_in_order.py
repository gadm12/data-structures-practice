def unique_in_order(sequence):
    prev = None
    results = []
    for char in sequence:

        if char != prev:
            results.append(char)
            prev = char

    return results


print(unique_in_order("AAAABBBCCDAABBB"))
