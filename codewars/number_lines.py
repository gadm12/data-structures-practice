def number(lines):

    # arr = []
    # for i, line in enumerate(lines, 1):
    #     arr.append(str(i) + ": " + line)
    # return arr
    return [str(i) + ": " + line for i, line in enumerate(lines, 1)]


print(number(["a", "b", "c"]))
