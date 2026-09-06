def how_much_coffee(events):

    count = 0
    for event in events:
        if event.lower() in ("cw", "cat", "dog", "movie"):
            if event.isupper():
                count += 2
            else:
                count += 1
    if count > 3:
        return "You need extra sleep"
    else:
        return count


print(how_much_coffee(["cw", "CAT", "DOG"]))
print(how_much_coffee(["cw"]))
