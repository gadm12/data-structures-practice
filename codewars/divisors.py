def divisors(integer):

    # result = list(filter(lambda n: integer % n == 0, range(2, integer)))
    # if len(result) == 0:
    #     return f"{integer} is prime"
    # return result
    return (
        list(filter(lambda n: integer % n == 0, range(2, integer)))
        or f"{integer} is prime"
    )


print(divisors(12))
print(divisors(13))
