def ordered_count(inp):
    counts = {}
    for char in inp:
        if char not in counts:
            counts[char] = 1
        else:
            counts[char] += 1
    return list(counts.items())


print(ordered_count("abracadabra"))
