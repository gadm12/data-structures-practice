def friend(x):
    buddies = []
    for i in x:
        if len(i) == 4:
            buddies.append(i)
    return buddies


print(
    friend(
        [
            "Ryan",
            "Kieran",
            "Mark",
        ]
    )
)
