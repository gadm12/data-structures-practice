def reverse_words(text):

    return " ".join([t[::-1] for t in text.split(" ")])


print(reverse_words("  double  spaced  words  "))
