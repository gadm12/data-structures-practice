def odd_or_even(arr):
    if len(arr) == 0:
        return 0
    sum = 0
    for n in arr:
        sum += n
    if sum % 2 == 0:
        return "even"
    else:
        return "odd"


print(odd_or_even([0, 1, 2]))
