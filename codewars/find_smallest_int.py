def find_smallest_int(arr):

    smallest = arr[0]
    for i in arr:
        if i < smallest:
            smallest = i
    return smallest


print(find_smallest_int([78, 56, 232, 12, 11, 43]))

