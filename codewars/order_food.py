def order_food(lst):
    counts = {}

    for person in lst:
        counts[person["meal"]] = counts.get(person["meal"], 0) + 1
        # if person["meal"] not in counts:
        #     counts[person["meal"]] = 1
        # else:
        #     counts[person["meal"]] += 1

    return counts


print(
    order_food(
        [
            {
                "firstName": "Noah",
                "lastName": "M.",
                "country": "Switzerland",
                "continent": "Europe",
                "age": 19,
                "language": "C",
                "meal": "vegetarian",
            },
            {
                "firstName": "Anna",
                "lastName": "R.",
                "country": "Liechtenstein",
                "continent": "Europe",
                "age": 52,
                "language": "JavaScript",
                "meal": "standard",
            },
            {
                "firstName": "Ramona",
                "lastName": "R.",
                "country": "Paraguay",
                "continent": "Americas",
                "age": 29,
                "language": "Ruby",
                "meal": "vegan",
            },
            {
                "firstName": "George",
                "lastName": "B.",
                "country": "England",
                "continent": "Europe",
                "age": 81,
                "language": "C",
                "meal": "vegetarian",
            },
        ]
    )
)
