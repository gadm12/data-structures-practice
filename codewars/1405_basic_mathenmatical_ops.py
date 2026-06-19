def basic_op(operator, v1, v2):

    if operator == "+":
        return v1 + v2
    elif operator == "-":
        return v1 - v2
    elif operator == "/":
        return v1 / v2
    elif operator == "*":
        return v1 * v2


print(basic_op("+", 4, 7))
print(basic_op("/", 49, 7))
print(basic_op("-", 14, 7))
print(basic_op("*", 4, 7))
