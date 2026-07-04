def series_sum(n):

    total = 0
    dom = 1
    for i in range(1, n + 1):
        total += 1/dom
        dom += 3
    return f"{total:.2f}"

print(series_sum(3))
