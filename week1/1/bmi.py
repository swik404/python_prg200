weight = float(input("Enter weight in kg: "))
height_cm = float(input("Enter height in cm: "))

height_m = height_cm / 100
bmi = weight / (height_m ** 2)

print("BMI =", round(bmi, 1))