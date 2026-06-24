def merge_strings(first, second):

    smallest = min(len(first), len(second))
    print(smallest)

    for i in range(smallest, 0, -1):

        if first[-i:] == second[:i]:
            print(first[-i:])
            return first + second[i:]
    return first + second


print(merge_strings("abcde", "cdefgh"))

