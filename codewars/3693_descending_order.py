def descending_order(num):

    lst = list(str(num))

    for _ in range(len(lst)):
        for digit in range(len(lst) - 1):

            if lst[digit] < lst[digit + 1]:
                lst[digit], lst[digit + 1] = lst[digit + 1], lst[digit]

    return int("".join(lst))

    # return int("".join(desc_lst))


print(descending_order(123456789))
