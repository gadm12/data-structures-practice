def find_needle(haystack):

    for i in range(len(haystack)):
        if haystack[i] == "needle":

            return f"found the needle at position {i}"


print(
    find_needle(["3", "123124234", None, "needle", "world", "hay", 2, "3", True, False])
)
