def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

# Example usage:
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))
bmi = calculate_bmi(weight, height)

print(f"Your BMI is: {bmi:.2f}")

# Classification based on BMI category:
if bmi < 18.5:
    print("Underweight")
elif 18.5 <= bmi < 25:
    print("Normal")
elif 25 <= bmi < 30:
    print("Overweight")
else:
    print("Obese")
