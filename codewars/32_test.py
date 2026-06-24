def test(r):

    total = 0
    for grade in r:
        total += grade
    avg = round(total / len(r), 3)

    class_grades = {"h": 0, "a": 0, "l": 0}

    for grade in r:
        if grade >= 9:
            class_grades["h"] += 1
        elif grade >= 7:
            class_grades["a"] += 1
        else:
            class_grades["l"] += 1
    if class_grades["a"] == 0 and class_grades["l"] == 0:
        return [avg, class_grades, "They did well"]
    else:
        return [avg, class_grades]
    # return avg


print(test([10, 9, 9, 10, 9, 10, 9]))
print(test([3, 5, 6, 10, 8, 4, 10, 9]))
