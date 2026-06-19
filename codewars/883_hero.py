def hero(bullets, dragons):

    if bullets == 0:
        return False

    killed = bullets / 2

    if killed >= dragons:
        return True
    else:
        return False
    # return killed


print(hero(1500, 751))
