# Question 2: Online Store Discount System

purchase_amount = float(input("Enter total purchase amount (NPR): "))
member = input("Are you a loyalty member? (yes/no): ").strip().lower()

if purchase_amount < 0:
    print("Purchase amount cannot be negative.")
else:
    if purchase_amount < 1000:
        discount_rate = 0
    elif purchase_amount < 5000:
        discount_rate = 0.05
    elif purchase_amount < 15000:
        discount_rate = 0.10
    else:
        discount_rate = 0.20

    discounted_amount = purchase_amount - (purchase_amount * discount_rate)

    if member == "yes":
        discounted_amount = discounted_amount - (discounted_amount * 0.05)

    print(f"Original purchase amount: NPR {purchase_amount:.2f}")
    print(f"Final payable amount: NPR {discounted_amount:.2f}")
