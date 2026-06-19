def fake_bin(x):

    results = ""
    for digit in x:
        digit = int(digit)
        if digit >= 5:
            results += "1"
        else:
            results += "0"
    return results


print(fake_bin("45385593107843568"))
