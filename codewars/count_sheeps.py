def count_sheep(sheep):

    count = 0
    for i in sheep:
        if i == True:
            count = i + count

    return count


print(
    count_sheep(
        [
            True,
            True,
            True,
            False,
            True,
            True,
            True,
            True,
            True,
            False,
            True,
            False,
            True,
            False,
            False,
            True,
            True,
            True,
            True,
            True,
            False,
            False,
            True,
            True,
        ]
    )
)
