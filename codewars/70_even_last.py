def even_last(numbers):
    if len(numbers) == 0:
        return 0
    count = 0
    for i in range(0, len(numbers), 2):
        
        count += numbers[i] * numbers[-1]
        
    return count


print(even_last([2, 3, 4, 5]))
