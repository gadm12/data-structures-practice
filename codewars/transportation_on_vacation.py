def rental_car_cost(d):

    day = 40
    total = d * day

    if 6 >= d >= 3:
        total -= 20
    elif d >= 7:
        total -= 50

    return total


print(rental_car_cost(7))
