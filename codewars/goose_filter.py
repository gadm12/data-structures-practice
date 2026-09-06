geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]


def goose_filter(birds):

    lst = []
    for bird in birds:
        if bird not in geese:
            lst.append(bird)

    return lst


print(
    goose_filter(
        [
            "Mallard",
            "Hook Bill",
            "African",
            "Crested",
            "Pilgrim",
            "Toulouse",
            "Blue Swedish",
        ]
    )
)
