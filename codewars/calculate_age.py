from rich.traceback import install

install(show_locals=True)


def calculate_age(year_of_birth, current_year):

    age = current_year - year_of_birth
    if age == 0:
        return f"You were born this very year!"
    elif age > 0:
        return f"You are {age} year{"" if age == 1 else "s"} old"
    else:
        return f"You will be born in {abs(age)} year{""if abs(age) == 1 else "s"}."


print(calculate_age(2012, 2016))
print(calculate_age(1989, 2016))
print(calculate_age(2000, 2090))
print(calculate_age(2000, 1990))
print(calculate_age(2000, 2000))
print(calculate_age(2011, 2012))
print(calculate_age(2000, 1999))
print(calculate_age(2000, 1099))
