def fizz_buzz(n):

    return list(
        map(
            lambda i: (
                "FizzBuzz"
                if i % 3 == 0 and i % 5 == 0
                else "Fizz" if i % 3 == 0 else "Buzz" if i % 5 == 0 else i
            ),
            range(1, n + 1),
        )
    )


print(fizz_buzz(10))
