def kaprekar_split(n):

    square = str(n**2)
    for i in range(len(square) + 1):
        # left = square[:i]
        # right = square[i:]

        left_num = int(square[:i]) if square[:i] else 0
        right_num = int(square[i:]) if square[i:] else 0
        if left_num + right_num == n:
            return i
    return -1


print(kaprekar_split(2223))
