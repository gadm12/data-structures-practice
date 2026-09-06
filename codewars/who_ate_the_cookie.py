def cookie(x):
    name = None
    if isinstance(x, str):
        name = "Zach"
    elif (isinstance(x, float) or isinstance(x, int)) and not isinstance(x, bool):
        name = "Monica"
    else:
        name = "the dog"

    return f"Who ate the last cookie? It was {name}!"


print(cookie("Ryan"))
