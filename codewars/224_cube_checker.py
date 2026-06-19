def cube_checker(volume, side):

    if side < 1 or volume < 1:
        return False

    if volume == (side**3):
        return True
    else:
        return False


print(cube_checker(8, 2))
print(cube_checker(8, 3))
