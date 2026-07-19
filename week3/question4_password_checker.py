# Question 4: Password Strength Checker

passwords = [
    "hello",
    "Hello123",
    "H3ll0@World",
    "12345678",
    "MyP@ss!"
]

special_characters = "!@#$%^&*"

for password in passwords:
    missing_criteria = []

    has_uppercase = False
    has_lowercase = False
    has_digit = False
    has_special = False

    for character in password:
        if character.isupper():
            has_uppercase = True
        elif character.islower():
            has_lowercase = True
        elif character.isdigit():
            has_digit = True

        if character in special_characters:
            has_special = True

    if len(password) < 8:
        missing_criteria.append("at least 8 characters")
    if not has_uppercase:
        missing_criteria.append("one uppercase letter")
    if not has_lowercase:
        missing_criteria.append("one lowercase letter")
    if not has_digit:
        missing_criteria.append("one digit")
    if not has_special:
        missing_criteria.append("one special character from !@#$%^&*")

    print(f"\nPassword: {password}")

    if len(missing_criteria) == 0:
        print("Strong password.")
    else:
        print("Weak password.")
        print("Missing criteria:")

        for criterion in missing_criteria:
            print(f"- {criterion}")
