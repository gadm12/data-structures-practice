def get_number(word):
    for char in word:
        if char.isdigit():
            return int(char)

def order(sentence):
    words = sentence.split()
    return " ".join(sorted(words, key=get_number))

print(order("is2 Thi1s T4est 3a"))
    
