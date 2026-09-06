def most_frequent_item_count(collection):

    if len(collection) == 0:
        return 0

    count = {}

    for n in collection:
        if n not in count:
            count[n] = 1
        else:
            count[n] += 1

    return max(count.values())


print(most_frequent_item_count([3, -1, -1, -1, 2, 3, -1, 3, -1, 2, 4, 9, 3]))
