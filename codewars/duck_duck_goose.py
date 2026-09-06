def duck_duck_goose(players, goose):
    res = goose % len(players)
    return players[res - 1].name


print(duck_duck_goose(["a", "b", "c", "d"], 1))
