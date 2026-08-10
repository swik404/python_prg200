from discount import final_price, TAX_RATE

products = [
    ("Laptop", 85000, 10),
    ("Headphones", 4500, 15),
    ("Phone Case", 800, 5),
    ("USB Cable", 600, 0),
]

print("TAX_RATE:", TAX_RATE)

for product_name, original_price, discount_pct in products:
    final = final_price(original_price, discount_pct)
    print(
        product_name,
        "- Original Price: NPR",
        original_price,
        "- Final Price: NPR",
        round(final, 2),
    )
