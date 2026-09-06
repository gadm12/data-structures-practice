def square_digits(num):

    tot = ""

    for digit in str(num):
        squ = int(digit) * int(digit)
        tot += str(squ)

    return int(tot)


print(square_digits(9119))
