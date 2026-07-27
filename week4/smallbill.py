# Question 1 - Small Shop Billing and Inventory System

inventory = {
    "rice": {"price": 120, "stock": 20},
    "milk": {"price": 90, "stock": 10},
    "bread": {"price": 60, "stock": 15},
    "eggs": {"price": 15, "stock": 30}
}

cart = {
    "rice": 2,
    "milk": 3,
    "eggs": 12
}


def process_order(inventory, cart):
    grand_total = 0
    purchased_items = []

    print("---- Bill ----")

    for item, quantity in cart.items():
        if item not in inventory:
            print(f"{item} is not available in the shop")
            continue

        available_stock = inventory[item]["stock"]

        if quantity <= available_stock:
            price = inventory[item]["price"]
            item_total = price * quantity

            grand_total += item_total
            inventory[item]["stock"] -= quantity

            purchased_items.append((item, quantity, item_total))
            print(f"{item} x{quantity} = NPR {item_total}")
        else:
            print(f"Sorry, not enough stock for {item}")

    print(f"Grand Total: NPR {grand_total}")
    print("--------------")

    print("Updated stock:")
    for item, details in inventory.items():
        print(f"{item}={details['stock']}", end="  ")

    print()


process_order(inventory, cart)
