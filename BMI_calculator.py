def calculate_bmi(weight, height):

    return weight / (height * height)


# ger usre input
weight = float(input("Enter your weight in Kilograms "))
height = float(input("Enter your height in meters "))

bmi = calculate_bmi(weight, height)
print(f"The BMI is {bmi:.2f}")
if bmi < 18.5:
    print("Underweight: BMI is less than 18.5")
elif 18.5 <= bmi <= 24.9:
    print("Normal weight: BMI is 18.5 to 24.9")
elif 25 <= bmi <= 29.9:
    print("Overweight: BMI is 25 to 29.9")
else:
    print("Obesity: BMI is 30 or greater")
