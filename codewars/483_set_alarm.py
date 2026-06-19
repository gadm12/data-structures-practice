def set_alarm(employed, vacation):

    if employed and vacation:
        return False
    elif not employed and vacation:
        return False
    elif not employed and not vacation:
        return False
    else:
        return True


print(set_alarm(True, True))
