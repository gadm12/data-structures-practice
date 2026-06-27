def is_same_language(lst):

    target_language = lst[0]["language"]
    matching = True
    print(target_language)

    for person in lst:
        if person["language"] != target_language:
            matching = False
    return matching


print(
    is_same_language(
        [
            {
                "firstName": "Daniel",
                "lastName": "J.",
                "country": "Aruba",
                "continent": "Americas",
                "age": 42,
                "language": "JavaScript",
            },
            {
                "firstName": "Kseniya",
                "lastName": "T.",
                "country": "Belarus",
                "continent": "Europe",
                "age": 22,
                "language": "JavaScript",
            },
            {
                "firstName": "Hanna",
                "lastName": "L.",
                "country": "Hungary",
                "continent": "Europe",
                "age": 65,
                "language": "JavaScript",
            },
        ]
    )
)
