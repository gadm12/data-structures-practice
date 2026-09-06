def dig_pow(n, p):
    total = 0
    power = p

    for digit in str(n):
        total += int(digit) ** power
        power += 1

    if total % n == 0:
        return total // n
    else:
        return -1


print(dig_pow(89, 1))
print(dig_pow(92, 1))
print(dig_pow(46288, 3))

print(2360688 // 46288)

