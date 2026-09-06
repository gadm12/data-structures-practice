def is_pangram(st):

    # seen = set()
    # for i in st.lower():
    #     if i.isalpha():
    #         seen.add(i)
    # return len(seen) == 26
    return len(set(i for i in st.lower() if i.isalpha())) == 26


print(is_pangram("The quick brown fox jumps over the lazy dog"))
print(is_pangram("abcdefghijklm opqrstuvwxyz"))
