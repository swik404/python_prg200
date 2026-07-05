cost_price = float(input("Cost per plate: "))
selling_price = float(input("Selling price per plate: "))
plates_sold = int(input("Plates sold today: "))

total_revenue = selling_price * plates_sold
total_cost = cost_price * plates_sold
profit = total_revenue - total_cost

profit_margin = (profit / total_revenue) * 100

print(f"Total revenue: Rs {total_revenue:.2f}")

print(f"Total cost:    Rs {total_cost:.2f}")
print(f"Total profit:  Rs {profit:.2f}")
print(f"Profit margin: {profit_margin:.1f}%")