def meeting(s):
    people = s.split(";")

    result = []

    for person in people:
        first, last = person.split(":")
        print(first, last)

        formatted = f"({last.upper()}, {first.upper()})"

        result.append(formatted)

    result.sort()

    return "".join(result)


print(
    meeting(
        "Fred:Corwill;Wilfred:Corwill;Barney:Tornbull;Betty:Tornbull;Bjon:Tornbull;Raphael:Corwill;Alfred:Corwill"
    )
)
