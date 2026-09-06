def better_than_average(class_points, your_points):

    total = your_points
    for i in class_points:
        total = total + i

    avg = total / (len(class_points) + 1)
    print(total)
    print(avg)
    if your_points > avg:
        return True
    else:
        return False


print(better_than_average([100, 40, 34, 57, 29, 72, 57, 88], 75))
