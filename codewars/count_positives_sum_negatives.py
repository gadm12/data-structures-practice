def count_positives_sum_negatives(arr):

    count = 0
    sum = 0
    if arr is None or len(arr) == 0:
        return []

    for num in arr:
        if num > 0:
            count += 1

        elif num < 0:
            sum += num

    return [count, sum]


print(
    count_positives_sum_negatives(
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]
    )
)
