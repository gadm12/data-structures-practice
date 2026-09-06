def are_you_playing_bingo(name):

    if name.lower().startswith("r"):

        return f"{name} plays banjo"
    else:
        return f"{name} does not play banjo"


print(are_you_playing_bingo("Rikke"))
print(are_you_playing_bingo("rolf"))
print(are_you_playing_bingo("martin"))
