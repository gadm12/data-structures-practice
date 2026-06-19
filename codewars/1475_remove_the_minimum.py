def remove_smallest(numbers):
    if len(numbers) == 0:
        return []
    
    nums = numbers.copy()

    smallest = nums[0]
    for num in nums:
        if num < smallest:
            smallest = num
    nums.remove(smallest)
    return nums


print(remove_smallest([5, 3, 2, 1, 4]))
