print("====================================")

print("     Foreign Remittance Converter   ")
print("====================================")




  usd_amount = float(input("Enter USD amount sent: "))

exchange_rate = float(input("Enter current exchange rate: "))

fee_percentage = float(input("Enter service fee percentage: "))




converted_amount = usd_amount * exchange_rate




fee_charged = converted_amount * fee_percentage / 100




final_amount = converted_amount - fee_charged




print()
print("------------- Result -------------")
print()

print(f"USD Amount Sent        : ${usd_amount:.2f}")

print(f"Exchange Rate          : NPR {exchange_rate:.2f}")

print(f"Converted NPR Amount   : NPR {converted_amount:.2f}")

print(f"Service Fee Percentage : {fee_percentage:.2f}%")

print(f"Fee Charged            : NPR {fee_charged:.2f}")

print(f"Final Amount Received  : NPR {final_amount:.2f}")

print()
print("----------------------------------")
print("Thank you for using the converter.")
print("----------------------------------")