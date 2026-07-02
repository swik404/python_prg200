print("Dashain Bonus Calculator")

salary = float(input("Enter monthly basic salary: "))

deduction_percent = float(input("Enter deduction percentage: "))

bonus = salary

deduction = bonus * deduction_percent / 100

take_home_bonus = bonus - deduction

print()
print("Dashain bonus:", bonus)
print("Deduction:", deduction)
print("Take home bonus:", take_home_bonus)