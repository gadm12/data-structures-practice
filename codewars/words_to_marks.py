def words_to_marks(s):
    count = 0
    for l in s:
        count += (ord(l)-(ord("a")-1))
    return count

print(words_to_marks('attitude'))