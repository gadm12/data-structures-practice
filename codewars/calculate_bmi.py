def bmi(weight, height):

    total = weight / (height**2)

    if total <= 18.5:
        return "Underweight"
    elif total <= 25.0:
        return "Normal"
    elif total <= 30.0:
        return "Overweight"
    else:
        return "Obese"


print(bmi(50, 1.80))
print(bmi(80, 1.80))
print(bmi(90, 1.80))
print(bmi(100, 1.80))
