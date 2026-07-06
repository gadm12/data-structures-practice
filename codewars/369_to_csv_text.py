def to_csv_text(array):

    # rows = []
    # for row in array:
    #     rows.append(",".join(str(num) for num in row))
    # return "\n".join(rows)
    return "\n".join(",".join(str(num) for num in row) for row in array)


print(
    to_csv_text(
        [
            [0, 1, 2, 3, 45],
            [10, 11, 12, 13, 14],
            [20, 21, 22, 23, 24],
            [30, 31, 32, 33, 34],
        ]
    )
)
