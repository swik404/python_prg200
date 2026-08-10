import random

random.seed(42)

friends = ["Ramesh", "Sunita", "Bikash", "Anjali", "Dipak"]
total_bill = 3750

def split_bill(friends, total):
    return total / len(friends)

def pick_lucky(friends):
    return random.choice(friends)

def final_summary(friends, total):
    share = split_bill(friends, total)
    lucky_person = pick_lucky(friends)

    for friend in friends:
        print(friend, "pays NPR", round(share, 2))

    print("Lucky person:", lucky_person)

    lucky_total = share + 50  # local variable
    print(lucky_person, "pays NPR", round(lucky_total, 2), "including lucky tax")

final_summary(friends, total_bill)
