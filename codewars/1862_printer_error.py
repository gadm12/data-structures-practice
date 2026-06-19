def printer_error(s):

    errors = 0

    for char in s:
        if char > "m":
            errors += 1
    return f"{str(errors)}/{str(len(s))}"


print(printer_error("aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz"))
