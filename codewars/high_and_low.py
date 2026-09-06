def high_and_low(numbers):

    return f"{max([int(n) for n in numbers.split()])} {min([int(n) for n in numbers.split()])}"


print(high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4"))

# def high_and_low(numbers):
    # numbers = numbers.split()
    # lst = [int(n) for n in numbers.split()]

    # high = lst[0]
    # low = lst[0]
    # for num in lst:

    #     if num < low:
    #         low = num
    #     if num > high:
    #         high = num

    # return f"{high} {low}"
# print(high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4"))