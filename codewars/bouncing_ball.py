def bouncing_ball(h, bounce, window):

    if h <= 0 or bounce <= 0 or bounce >= 1 or window >= h:
        return -1

    count = 1
    h = h * bounce
    while h > window:
        count += 2
        h = h * bounce
    return count


print(bouncing_ball(30, 0.66, 1.5))
