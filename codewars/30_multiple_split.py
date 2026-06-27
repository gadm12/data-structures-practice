def multiple_split(string, delimiters=[]):
    
    if not string:
        return []
    elif not delimiters:
        return [string]
    else:
        for a in delimiters:
            string = string.replace(a, " ")

    return string.split()


print(multiple_split("Hi, how are you?", [" "]))
print(multiple_split("1+2-3", ["+", "-"]))
