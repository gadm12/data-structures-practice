def find_average(nums):

    total = 0
    for n in nums:
        total += n
    avg = total / len(nums)
    return avg


print(find_average([1, 3, 5, 7]))
