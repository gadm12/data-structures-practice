def remove_bmw(string):

    if not isinstance(string, str):
        raise TypeError("This program only works for text.")

    results = ""

    for char in string:
        if char not in {"b", "m", "w", "B", "M", "W"}:
            results += char

    return results


print(remove_bmw("bmwvolvoBMW"))
