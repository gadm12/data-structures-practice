def find_average(numbers):

    if len(numbers) == 0:
        return 0

    total = 0
    for number in numbers:
        total += number
    avg = total / len(numbers)
    return avg


print(find_average([]))
print(find_average([1, 2, 3]))
