def nb_dig(n, d):
    count = 0
    
    for num in range(n + 1):
        square = num **2
        square = str(square)
        count += square.count(str(d))
    return count


print(nb_dig(5750, 0))
