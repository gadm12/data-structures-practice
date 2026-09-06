def how_much_i_love_you(nb_petals):

    phrases = ["I love you", "a little", "a lot", "passionately", "madly", "not at all"]
    res = nb_petals % 6
    return phrases[res - 1]


print(how_much_i_love_you(7))
