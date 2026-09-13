def row_sum_odd_numbers(n):
    for i in range(1, n + 1):
        if i == n:
            return sum(range(i ** 2 - i + 1, i ** 2 + i, 2))
    
print(row_sum_odd_numbers(41))