def find_next_square(sq):

    res = sq ** (1 / 2)
    
    if sq / int(res) == int(res):
        next_sq = (res + 1) * (res + 1)
        
        return int(next_sq)
    else:
        return -1


print(find_next_square(121))

print(find_next_square(144))

print(find_next_square(155))
