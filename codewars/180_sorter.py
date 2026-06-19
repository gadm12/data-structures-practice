def sorter(textbooks):

    for i in range(len(textbooks)):
        for j in range(len(textbooks) - 1):
            if textbooks[j].lower() > textbooks[j + 1].lower():
                textbooks[j], textbooks[j + 1] = textbooks[j + 1], textbooks[j]
    return textbooks
    #return sorted(textbooks, key=str.lower)


print(sorter(["Algebra", "History", "Geometry", "English"]))
