def sum_pairs(ints, s):

    seen = set()
    for num in ints:
        diff = s - num

        if diff in seen:
            return [diff, num]
        seen.add(num)

    return None


print(sum_pairs([10, 5, 2, 3, 7, 5], 10))
