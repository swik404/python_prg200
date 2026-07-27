# Question 5 - Simple ATM Simulator

accounts = {
    "A001": {
        "name": "Ramesh Thapa",
        "balance": 15000,
        "pin": "1234"
    },
    "A002": {
        "name": "Sunita Karki",
        "balance": 8500,
        "pin": "5678"
    },
    "A003": {
        "name": "Bikash Rai",
        "balance": 22000,
        "pin": "9012"
    }
}


def atm(account_id, pin, action, amount=0):
    if account_id not in accounts:
        print("Account not found")
        return

    account = accounts[account_id]

    if pin != account["pin"]:
        print("Incorrect PIN")
        return

    if action == "balance":
        print(f"Account holder: {account['name']}")
        print(f"Current balance: NPR {account['balance']}")

    elif action == "deposit":
        if amount <= 0:
            print("Deposit amount must be greater than zero")
            return

        account["balance"] += amount
        print(f"Deposit successful: NPR {amount}")
        print(f"New balance: NPR {account['balance']}")

    elif action == "withdraw":
        if amount <= 0:
            print("Withdrawal amount must be greater than zero")
        elif amount > account["balance"]:
            print("Insufficient funds")
        else:
            account["balance"] -= amount
            print(f"Withdrawal successful: NPR {amount}")
            print(f"New balance: NPR {account['balance']}")

    else:
        print("Invalid action")


atm("A001", "1234", "balance")
print()

atm("A002", "0000", "withdraw", 2000)
print()

atm("A002", "5678", "deposit", 3000)
print()

atm("A003", "9012", "withdraw", 25000)
print()

atm("A004", "1111", "balance")
