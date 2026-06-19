def high_and_low(numbers):

    arr = numbers.split()
    arr2 = []
    for digit in arr:
        digit = int(digit)
        arr2.append(digit)

    hi = arr2[0]
    lo = arr2[0]

    for num in arr2:
        if num < lo:
            lo = num
        elif num > hi:
            hi = num
    return f"{str(hi)} {str(lo)}"


print(high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4"))
