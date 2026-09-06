def sum_two_smallest_numbers(numbers):

    smallest = min(numbers[0], numbers[1])
    smallest_2 = max(numbers[0], numbers[1])

    for n in numbers[2:]:
        if n < smallest:
            smallest_2 = smallest
            smallest = n
        elif n < smallest_2:
            smallest_2 = n

    return smallest + smallest_2


print(sum_two_smallest_numbers([19, 5, 42, 2, 77]))
print(sum_two_smallest_numbers([7, 15, 12, 18, 22]))
