def enough(cap, on, wait):

    remaining = (on + wait) - cap
    if on + wait > cap:
        return remaining
    else:
        return 0
    


print(enough(10, 5, 5))
print(enough(100, 60, 50))
