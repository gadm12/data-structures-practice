def number(bus_stops):

    total = 0

    for enters, leaves in bus_stops:
        total = (enters - leaves) + total

    return total


print(number([[10, 0], [3, 5], [5, 8]]))
print(number([[3, 0], [9, 1], [4, 10], [12, 2], [6, 1], [7, 10]]))
