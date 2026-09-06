def minimum(arr):
    smallest = arr[0]

    for num in arr:
        if num < smallest:
            smallest = num
    return smallest


def maximum(arr):
    largest = arr[0]

    for num in arr:
        if num > largest:
            largest = num
    return largest


print(maximum([-52, 56, 30, 29, -54, 0, -110]))
print(minimum([-52, 56, 30, 29, -54, 0, -110]))
