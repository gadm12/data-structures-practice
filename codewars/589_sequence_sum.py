def sequence_sum(begin_number, end_number, step):
    total = 0
    for num in range(begin_number, end_number + 1, step):
        total += num
    return total


print(sequence_sum(2, 6, 2))
