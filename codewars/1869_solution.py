def solution(text, ending):

    lst = []

    for char in range(len(text) - len(ending), len(text), 1):
        lst.append(text[char])

    last = "".join(lst)
    if last == ending:
        return True

    else:
        return False


print(solution("samurai", "ai"))
