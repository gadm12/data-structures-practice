def solution(string):
    word = []
    for i in range(len(string) - 1, -1, -1):
        word.append(string[i])

    return "".join(word)


print(solution("word"))
