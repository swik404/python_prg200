print("Trekking Permit Cost Calculator")

trekkers = int(input("Enter number of trekkers: "))

tims = int(input("Enter TIMS fee per person: "))
acap = int(input("Enter ACAP fee per person: "))

cost_per_person = tims + acap

total_cost = cost_per_person * trekkers

service_charge = total_cost * 5 / 100

final_total = total_cost + service_charge

average_cost = final_total / trekkers

print()
print("Total cost for group:", final_total)
print("Average cost per person:", average_cost)