def two_sum(numbers, target):

    seen = {}
    for i, num in enumerate(numbers):
        diff = target - num
        if diff in seen:
            return i, seen[diff]
        seen[num] = i
    return []


print(two_sum([1, 2, 3], 4))
print(two_sum([3, 2, 4], 6))
