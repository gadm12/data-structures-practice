def small_enough(array,limit):
    
    for num in array:
        if num > limit:
            return False
    return True
    
print(small_enough([[78, 117, 110, 99, 104, 117, 107, 115] ,100]))

print(small_enough([[1, 2, 3, 4, 5, 6, 7, 8, 9] ,10]))
