def get_average(lst):

    sum = 0
    for person in lst:

        sum += person["age"]
    avg = sum / len(lst)

    return round(avg)


print(
    get_average(
        [
            {
                "firstName": "Maria",
                "lastName": "Y.",
                "country": "Cyprus",
                "continent": "Europe",
                "age": 30,
                "language": "Java",
            },
            {
                "firstName": "Victoria",
                "lastName": "T.",
                "country": "Puerto Rico",
                "continent": "Americas",
                "age": 70,
                "language": "Python",
            },
        ]
    )
)
