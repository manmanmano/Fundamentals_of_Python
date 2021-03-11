def bmi_calculator(weight):
    if weight < 18.5:
        return "underweight"
    elif weight >= 18.5 and weight <= 24.9:
        return "normal weight"
    elif weight >= 25 and weight <= 29.9:
        return "overweight"
    else:
        return "obesity"

weight = float(input("Enter your weight: "))
while weight < 0:
        print("INVALID INPUT - weight must be positive!")
        weight = float(input("\nEnter your weight: "))
print("Your BMI category is:", bmi_calculator(weight).upper())


