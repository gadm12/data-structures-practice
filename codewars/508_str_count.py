def str_count(strng, letter):
    sum = []
    for char in range(len(strng)):
        if letter == strng[char]:
            sum.append(strng[char])
    return len(sum)




print(str_count("hello", "l"))
print(str_count("ggggg", "g"))
