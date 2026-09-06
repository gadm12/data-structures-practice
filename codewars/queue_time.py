from rich.traceback import install

install(show_locals=True)


def queue_time(customers, n):

    tills = [0] * n
    for time in customers:
        smallest = tills.index(min(tills))
        tills[smallest] += time

    return max(tills)


print(queue_time([49, 42, 1, 32, 30, 6, 16, 48, 33, 37, 47, 15, 20], 5))  # 89
print(queue_time([2, 2, 3, 3, 4, 4], 2))  # 9
print(queue_time([2, 3, 10], 3))  # 12
print(queue_time([10, 3, 2], 2))  # 10
print(queue_time([1, 2, 3, 4, 5], 100))  # 5
