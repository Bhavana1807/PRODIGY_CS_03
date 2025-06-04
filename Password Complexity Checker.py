import re

def check_password_strength(password):
    length = len(password) >= 8
    lowercase = re.search(r"[a-z]", password)
    uppercase = re.search(r"[A-Z]", password)
    digit = re.search(r"\d", password)
    special = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)

    score = sum([bool(length), bool(lowercase), bool(uppercase), bool(digit), bool(special)])

    if score == 5:
        strength = "Very Strong"
    elif score == 4:
        strength = "Strong"
    elif score == 3:
        strength = "Moderate"
    elif score == 2:
        strength = "Weak"
    else:
        strength = "Very Weak"

    print(f"\nPassword Strength: {strength}")
    print("Feedback:")
    if not length:
        print("- Password should be at least 8 characters long.")
    if not lowercase:
        print("- Add lowercase letters.")
    if not uppercase:
        print("- Add uppercase letters.")
    if not digit:
        print("- Add numbers.")
    if not special:
        print("- Add special characters (!@#$ etc.)")

# Main
print("Password Strength Checker")
user_password = input("Enter your password: ")
check_password_strength(user_password)